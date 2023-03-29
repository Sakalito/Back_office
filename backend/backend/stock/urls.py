from django.urls import path

from .views import StockMoveListView, StockMoveCreateView, StockMoveDetailView, StockMoveItemListView

urlpatterns = [
    path("stock/", StockMoveListView.as_view()),
    path("stock/move/create/", StockMoveCreateView.as_view()),
    path("stock/move/<int:pk>/", StockMoveDetailView.as_view()),
    path("stock/move/items", StockMoveItemListView.as_view()),
]
