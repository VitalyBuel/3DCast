from django.urls import path
from .models import Post


urlpatterns = [
    path('index', index)
]
