from django.urls import path
<<<<<<< HEAD
from .views import index, detail, News
=======
from .views import index, detail, Post_news
>>>>>>> 531554b77c8dafecbdc65beff8ecd24e00865fc6

urlpatterns = [
    path('news/', index, name='index'),
    path('news/<int:pk>/', detail, name='detail'),
<<<<<<< HEAD
    path('news/search', News),
=======
    path('news/search', Post_news, name='Post_news'),
>>>>>>> 531554b77c8dafecbdc65beff8ecd24e00865fc6
]