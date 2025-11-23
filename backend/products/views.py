from django.shortcuts import render
from .models import Poster,Product,Category,Unit
from .serializers import PosterSerializer,ProductSerializer,UnitSerializer,CategorySerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class Posterview(generics.ListCreateAPIView):
    queryset = Poster.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class UnitListView(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]

class UnitRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductRetrieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
