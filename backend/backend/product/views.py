from django.shortcuts import render

from rest_framework import generics, permissions

from .models import ProductModel
from .serializers import ProduitSerializer

# Create your views here.


class ProductListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ProductModel.objects.all()
    serializer_class = ProduitSerializer


class ProductCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductModel.objects.all()
    serializer_class = ProduitSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProduitSerializer
