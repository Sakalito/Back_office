from django.urls import path

from .views import ImageListView, ImageDetailView, ImageCreateView, ProductImageListView, ImageRenderedView

urlpatterns = [
    path('images/', ImageListView.as_view()),
    path('image/create/', ImageCreateView.as_view()),
    path('image/rendered/<int:pk>/', ImageRenderedView.as_view()),
    path('image/<int:pk>/', ImageDetailView.as_view()),
    path('product/<int:pk>/images/', ProductImageListView.as_view()),
]
