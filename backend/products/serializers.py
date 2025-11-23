from rest_framework import serializers
from .models import Category,Poster,Product,Unit

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ('id', 'image', 'created_at')
        read_only_fields = ('id','created_at')

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"