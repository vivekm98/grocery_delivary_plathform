from django.shortcuts import render
from .models import Cart
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import CartSerializer
# Create your views here.
class CartListView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class CartRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]