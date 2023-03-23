from django.urls import path

from .views import DiscountListView, DiscountDetailView, DiscountCreateView, DiscountUpdateView, DiscountDeleteView, ProductDiscountListView

urlpatterns = [
    path('discounts/', DiscountListView.as_view()),
    path('discount/<int:pk>/', DiscountDetailView.as_view()),
    path('discount/create/', DiscountCreateView.as_view()),
    path('discount/update/<int:pk>/', DiscountUpdateView.as_view()),
    path('discount/delete/<int:pk>/', DiscountDeleteView.as_view()),
    path('discounts/product/<int:pk>/', ProductDiscountListView.as_view()),
]
