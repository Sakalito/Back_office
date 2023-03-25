from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response

from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView

from .renderers import JPEGRenderer, PNGRenderer
from .models import ImageModel
from .serializers import ImageSerializer


# Create your views here.


class ProductImageListView(generics.GenericAPIView, mixins.ListModelMixin):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(product__id=kwargs["pk"])
        return self.list(request, *args, **kwargs)


class ImageListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer


class ImageCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer


class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer


class ImageRenderedView(APIView):
    renderer_classes = (PNGRenderer, JPEGRenderer,)

    def get(self, request, pk, **kwargs):
        try:
            image = ImageModel.objects.filter(id=pk).first()
            return Response(image.img)
        except:
            raise Http404
