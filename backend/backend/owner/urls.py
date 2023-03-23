from django.urls import path

from .views import ProductOwnerListView, ProductOwnerDetailView, ProductOwnerCreateView

urlpatterns = [
    path('owners', ProductOwnerListView.as_view()),
    path('owner/<int:pk>/', ProductOwnerDetailView.as_view()),
    path('owner/create/', ProductOwnerCreateView.as_view()),
]