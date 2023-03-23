from django.urls import path

from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('product/create/', ProductCreateView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('product/update/<int:pk>/', ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view()),
    # categories
    path('product/categories', CategoryListView.as_view()),
    path('product/category/<int:pk>/', CategoryDetailView.as_view()),
    path('product/category/<int:pk>/', CategoryView.as_view()),
]
