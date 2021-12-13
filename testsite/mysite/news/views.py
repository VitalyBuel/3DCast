from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    news = News.objects.order_by('-created_at')
    context = {'news': news,
               'title': 'List news'
               }
    return render(request, template_name='news/index.html', context=context)
