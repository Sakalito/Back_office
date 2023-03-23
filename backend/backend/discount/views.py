from django.shortcuts import render

from rest_framework import generics, mixins, permissions

from .models import DiscountModel
from .serializers import DiscountSerializer


# Create your views here.

class ProductDiscountListView(generics.GenericAPIView, mixins.ListModelMixin):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = DiscountModel.objects.all()
    serializer_class = DiscountSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(product__id=kwargs["pk"])
        return self.list(request, *args, **kwargs)
    

class DiscountListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = DiscountModel.objects.all()
    serializer_class = DiscountSerializer

class DiscountDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DiscountModel.objects.all()
    serializer_class = DiscountSerializer

class DiscountCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DiscountModel.objects.all()
    serializer_class = DiscountSerializer

class DiscountUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DiscountModel.objects.all()
    serializer_class = DiscountSerializer

class DiscountDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DiscountModel.objects.all()
    serializer_class = DiscountSerializer
