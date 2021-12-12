from django.shortcuts import render
from django.views.generic import ListView
<<<<<<< HEAD
=======
from django.core.paginator import Paginator
>>>>>>> 531554b77c8dafecbdc65beff8ecd24e00865fc6
from .models import *


def index(request):
    news = Post.objects.all()[::-1]
    return render(request, 'default.html', context={'news': news})


def detail(request, pk):
    new = Post.objects.get(pk__iexact=pk)
    return render(request, 'details.html', context={'new': new})

<<<<<<< HEAD
class News(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    ordering = ['-rating']
    paginate_by = 1
=======

class Post_news(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'post'
    ordering = ['dateCreation']
    paginate_by = 1
>>>>>>> 531554b77c8dafecbdc65beff8ecd24e00865fc6
