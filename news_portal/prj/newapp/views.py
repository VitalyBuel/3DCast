from django.shortcuts import render
from .models import *
<<<<<<< HEAD


def index(request):
    news = Post.objects.all()[::-1]
    return render(request, 'default.html', context={'news': news})


def detail(request, pk):
    new = Post.objects.get(pk__iexact=pk)
    return render(request, 'details.html', context={'new': new})
=======

def index(request):
    news = Post.objects.all()
    return render(request, 'index.html', context={'news': news})

def detail(request, pk):
    new = Post.objects.get(pk=pk)
    return render(request, 'details.html', context={'new': new})
>>>>>>> 4c0ec9193bc7e3f3fbbc097d6ec02758360cad75
