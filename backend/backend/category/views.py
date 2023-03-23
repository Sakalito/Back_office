from django.shortcuts import render

from rest_framework import generics, permissions

from backend.mixins import BackendDetailMixin

from .serializers import CategorySerializer
from .models import CategoryModel

# Create your views here.


class CategoryListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(BackendDetailMixin):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
