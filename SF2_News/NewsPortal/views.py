from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .forms import PostForm
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    ordering = '-date_added'
    template_name = 'NewsPortal/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(type='N')
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'News'
        return context


class ArticleList(ListView):
    model = Post
    ordering = '-date_added'
    template_name = 'NewsPortal/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(type='A')
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Article'
        return context


class PostDetail(DetailView):
    model = Post
    context_object_name = 'news'
    template_name = 'NewsPortal/post_detail.html'


def home(request):
    # А код вы точно смотрите?
    return render(request, 'NewsPortal/index.html')


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'NewsPortal/post_edit.html'


class PostSearch(ListView):
    model = Post
    template_name = 'NewsPortal/post_search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'NewsPortal/post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'NewsPortal/post_delete.html'
    success_url = reverse_lazy('news_portal:home')
