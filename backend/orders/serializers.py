from rest_framework import serializers
from .models import DeliverySlot,Order,OrderItem


class DeliverySlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliverySlot
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    class Meta:
        model = OrderItem
        fields = ['id','product','quantity','price_at_order','total_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    total_price = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields = ['id','user','slot','status','created_at','items','total_price']

