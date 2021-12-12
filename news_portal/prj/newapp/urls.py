from django.urls import path
from .views import index, detail, News

urlpatterns = [
    path('news/', index, name='index'),
    path('news/<int:pk>/', detail, name='detail'),
    path('news/search', News),
]