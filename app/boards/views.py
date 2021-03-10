from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .board import Board
from .post import Post


class BoardListVIew(ListView):
    model = Board


class BoardDetailView(DetailView):
    model = Board

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['board_detail'] = Board.objects.get(slug=self.kwargs.get('slug'))
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_detail'] = Post.objects.get(pk=self.kwargs.get('pk'))
        return context


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'boards/post_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['board_detail'] = Board.objects.get(slug=self.kwargs.get('slug'))
        return context


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'boards/post_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['post_detail'] = Post.objects.get(pk=self.kwargs.get('pk'))
        return context
