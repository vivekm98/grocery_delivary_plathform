# serializers.py
from rest_framework import serializers
from .models import Cart
from products.serializers import ProductSerializer  # assuming you have one

from rest_framework import serializers
from .models import Cart
from products.models import Product
from products.serializers import ProductSerializer
from products.models import Product

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # for GET
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, source='product'
    )  # for POST

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'product_id', 'quantity']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        return Cart.objects.create(user=user, **validated_data)