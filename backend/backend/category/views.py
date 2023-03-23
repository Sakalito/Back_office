from django.shortcuts import render

from rest_framework import generics, mixins
from rest_framework import permissions

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


class CategoryDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
