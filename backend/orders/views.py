from django.shortcuts import render
from .models import DeliverySlot,Order,OrderItem
from .serializers import DeliverySlotSerializer,OrderSerializer,OrderItemSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.

class DeliverySlotListView(generics.ListCreateAPIView):
    queryset = DeliverySlot.objects.all()
    serializer_class = DeliverySlotSerializer
    permission_classes = [IsAuthenticated]

class DeliverySlotRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliverySlot.objects.all()
    serializer_class = DeliverySlotSerializer
    permission_classes = [IsAuthenticated]


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]



class OrderItemListView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

class OrderItemRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]


