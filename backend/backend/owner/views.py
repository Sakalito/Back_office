from django.shortcuts import render

from rest_framework import generics, permissions, mixins

from backend.mixins import BackendDetailMixin

from .models import ProductOwnerModel
from .serializers import ProductOwnerSerializer


# Create your views here.

class ProductOwnerListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ProductOwnerModel.objects.all()
    serializer_class = ProductOwnerSerializer


class ProductOwnerCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductOwnerModel.objects.all()
    serializer_class = ProductOwnerSerializer


class ProductOwnerDetailView(BackendDetailMixin):
    queryset = ProductOwnerModel.objects.all()
    serializer_class = ProductOwnerSerializer
