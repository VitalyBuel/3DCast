from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.template.loader import render_to_string
from celery import shared_task

from .models import PostCategory
from newspaper.settings import SITE_URL, DEFAULT_FROM_EMAIL
from .tasks import send_notifications


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications.delay(instance.preview(), instance.pk, instance.title, subscribers)