from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Cart, DeliverySlot, Order
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator



class UserSignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '_all_'


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = Cart
        fields = ('id', 'user', 'product', 'product_id', 'quantity')
        read_only_fields = ('user',)


class DeliverySlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliverySlot
        fields = '_all_'


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    slot_id = serializers.PrimaryKeyRelatedField(
        queryset=DeliverySlot.objects.all(), source='slot', write_only=True
    )

    class Meta:
        model = Order
        fields = ('id', 'user', 'slot', 'slot_id', 'total_price', 'status', 'created_at')
        read_only_fields = ('user', 'created_at', 'status', 'slot')