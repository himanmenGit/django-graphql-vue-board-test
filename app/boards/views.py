from django.views.generic import ListView, DetailView
from .board import Board


class BoardListVIew(ListView):
    model = Board


class BoardDetailView(DetailView):
    model = Board
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['board_detail'] = Board.objects.get(slug=self.kwargs.get('slug'))
        return context
