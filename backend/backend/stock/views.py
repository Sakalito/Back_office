from django.shortcuts import render

from rest_framework import generics, permissions

from .models import StockMoveModel, StockMoveItemModel
from .serializers import StockMoveItemSerializer, StockMoveSerializer

# Create your views here.


class StockMoveListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = StockMoveSerializer
    queryset = StockMoveModel.objects.all()


class StockMoveCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StockMoveSerializer
    queryset = StockMoveModel.objects.all()


class StockMoveDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StockMoveSerializer
    queryset = StockMoveModel.objects.all()


class StockMoveItemListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = StockMoveItemSerializer
    queryset = StockMoveItemModel.objects.all()


class StockMoveItemCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StockMoveItemSerializer
    queryset = StockMoveItemModel.objects.all()


class StockMoveItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StockMoveItemSerializer
    queryset = StockMoveItemModel.objects.all()
