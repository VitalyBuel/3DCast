from django.shortcuts import render
from .models import *


def index(request):
    news = Post.objects.all()[::-1]
    return render(request, 'default.html', context={'news': news})


def detail(request, pk):
    new = Post.objects.get(pk__iexact=pk)
    return render(request, 'details.html', context={'new': new})
