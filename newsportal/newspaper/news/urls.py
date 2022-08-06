from django.contrib import admin
from django.urls import path
from news.views import index
from .models import Post


urlpatterns = [
    path('index', index)
]