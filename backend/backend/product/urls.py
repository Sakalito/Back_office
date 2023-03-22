from django.urls import path

from .views import ProductListView, ProductDetailView, ProductCreateView

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('product/create/', ProductCreateView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]
