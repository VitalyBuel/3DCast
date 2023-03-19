from django.urls import path
from .views import *

urlpatterns = [
    path('news/', index, name='index'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news'),
    path('news/search', news_search, name='news_search'),
    path('news/create', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit', NewsUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete', NewsDelete.as_view(), name='news_delete'),
    path('article/create', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit', ArticleUpdate.as_view(), name='article_edit'),
    path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),
    path('profile/<int:pk>/update', ProfileUserUpdate.as_view(), name='profile'),
    path('news/categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('news/categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
