from django.urls import path
from .views import index, detail, Post_news

urlpatterns = [
    path('news/', index, name='index'),
    path('news/<int:pk>/', detail, name='detail'),
    path('news/search', Post_news, name='Post_news'),
]