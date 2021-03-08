from django.urls import path
from .views import BoardListVIew, BoardDetailView

urlpatterns = [
    path('', BoardListVIew.as_view(), name='board_list'),
    path('<slug:slug>', BoardDetailView.as_view(), name='board_detail')
]
