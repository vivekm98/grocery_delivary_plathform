from django.shortcuts import render
from .models import DeliverySlot,Order,OrderItem
from .serializers import DeliverySlotSerializer,OrderSerializer,OrderItemSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated

from rest_framework import generics, permissions
from .models import Order, OrderItem
from cart.models import Cart
from .serializers import OrderSerializer
# Create your views here.


class DeliverySlotListView(generics.ListCreateAPIView):
    queryset = DeliverySlot.objects.all()
    serializer_class = DeliverySlotSerializer
    permission_classes = [IsAuthenticated]

class DeliverySlotRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliverySlot.objects.all()
    serializer_class = DeliverySlotSerializer
    permission_classes = [IsAuthenticated]


class OrderCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only orders of the logged-in user
        return Order.objects.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        user = self.request.user
        cart_items = Cart.objects.filter(user=user)

        total = sum(item.product.price * item.quantity for item in cart_items)
        order = serializer.save(user=user, total_price=total)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price_at_order=item.product.price
            )

        cart_items.delete()

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


