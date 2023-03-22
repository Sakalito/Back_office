from django.shortcuts import render

from rest_framework import generics

from .models import ProduitModel
from .serializers import ProduitSerializer

# Create your views here.


class ProductListView(generics.ListAPIView):
    queryset = ProduitModel.objects.all()
    serializer_class = ProduitSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = ProduitModel.objects.all()
    serializer_class = ProduitSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = ProduitModel.objects.all()
    serializer_class = ProduitSerializer

