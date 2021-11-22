from django.shortcuts import render
from .models import *

def index(request):
    news = Post.objects.all()
    return render(request, 'index.html', context={'news': news})

def detail(request, pk):
    new = Post.objects.get(pk=pk)
    return render(request, 'details.html', context={'new': new})