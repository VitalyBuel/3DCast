from django.shortcuts import render
from django.views.generic import ListView
from .models import *


def index(request):
    news = Post.objects.all()[::-1]
    return render(request, 'default.html', context={'news': news})


def detail(request, pk):
    new = Post.objects.get(pk__iexact=pk)
    return render(request, 'details.html', context={'new': new})

class News(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    ordering = ['-rating']
    paginate_by = 1