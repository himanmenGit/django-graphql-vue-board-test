from django.urls import path
from .views import BoardListVIew, BoardDetailView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', BoardListVIew.as_view(), name='board_list'),
    path('<slug:slug>', BoardDetailView.as_view(), name='board_detail'),
    path('<slug:slug>/detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/create', PostCreateView.as_view(), name='post_create')
]
