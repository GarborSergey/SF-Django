from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post



class NewsList(ListView):
    model = Post
    ordering = '-date_added'
    template_name = 'NewsPortal/news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(type='N')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'News'
        return context

class PostDetail(DetailView):
    model = Post
    context_object_name = 'news'
    template_name = 'NewsPortal/news_detail.html'



class ArticlesList(ListView):
    model = Post
    ordering = '-date_added'
    template_name = 'NewsPortal/news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(type='A')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Article'
        return context

def home(request):
    return render(request, 'NewsPortal/index.html')