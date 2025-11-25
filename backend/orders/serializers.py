from rest_framework import serializers
from .models import DeliverySlot,Order,OrderItem


class DeliverySlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliverySlot
        fields = ['id','slot']
from rest_framework import serializers
from .models import Order, OrderItem, DeliverySlot
from products.serializers import ProductSerializer  # assuming you have this

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price_at_order', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  # include related items
    slot = serializers.StringRelatedField()  # optional: display slot name

    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'phone', 'address', 'slot', 'total_price', 'status', 'items']