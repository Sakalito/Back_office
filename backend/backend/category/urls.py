from django.urls import path

from .views import CategoryListView, CategoryDetailView, CategoryCreateView

urlpatterns = [
    path('categories', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
]