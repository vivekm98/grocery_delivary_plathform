from django.shortcuts import render
from .models import Poster,Product,Category,Unit
from .serializers import PosterSerializer,ProductSerializer,UnitSerializer,CategorySerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class Posterview(generics.ListCreateAPIView):
    queryset = Poster.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class UnitListView(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAdminUser]

class UnitRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAdminUser]


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]

class ProductRetrieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
