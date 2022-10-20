from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import NewsForm
from .models import *


def index(request):
    news = Post.objects.all()[::-1]
    paginator = Paginator(news, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'listnews.html', context={'page_obj': page_obj})


def detail(request, pk):
    new = Post.objects.get(pk__iexact=pk)
    return render(request, 'detail.html', context={'new': new})


def news_search(request):
    f = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'search.html', context={'filter': f})


class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('index')


class ArticleCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'article_edit.html'


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('index')