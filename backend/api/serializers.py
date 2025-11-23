# from rest_framework import serializers
# from .models import Category
# from .models import Unit
# from .models import Product
# from .models import Cart
# from .models import DeliverySlot
# from .models import Order
# from .models import OrderItem
# from .models import Subscription
# from .models import Poster
# from django.contrib.auth.models import User
#

#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['name']
#
# class PosterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Poster
#         fields = ('id', 'image', 'created_at')
#         read_only_fields = ('id','created_at')
#
# class UnitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Unit
#         fields = ['name']
#
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = "__all__"
#

#
# class DeliverySlotSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeliverySlot
#         fields = "__all__"
#
# class OrderItemSerializer(serializers.ModelSerializer):
#     total_price = serializers.ReadOnlyField()
#     class Meta:
#         model = OrderItem
#         fields = ['id','product','quantity','price_at_order','total_price']
#
# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True,read_only=True)
#     total_price = serializers.ReadOnlyField()
#     class Meta:
#         model = Order
#         fields = ['id','user','slot','status','created_at','items','total_price']
#

#
#
