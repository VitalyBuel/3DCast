from django.shortcuts import render
from .models import *


def index(request):
    news = Post.objects.all()[::-1]
    return render(request, 'default.html', context={'news': news})


def detail(request, id):
    new = Post.objects.get(id__iexact=id)
    return render(request, 'detail.html', context={'new': new})
