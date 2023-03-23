from django.shortcuts import render

from rest_framework import generics, permissions

from backend.mixins import BackendDetailMixin

from .models import ProduitModel
from .serializers import ProduitSerializer

# Create your views here.


class ProductListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ProduitModel.objects.all()
    serializer_class = ProduitSerializer


class ProductCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProduitModel.objects.all()
    serializer_class = ProduitSerializer


class ProductDetailView(BackendDetailMixin):
    queryset = ProduitModel.objects.all()
    serializer_class = ProduitSerializer
