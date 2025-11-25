from rest_framework import serializers
from .models import Category,Poster,Product,Unit

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','description','image']

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
    unit_name = serializers.CharField(source='unit.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','description','price','unit_name','category_name','stock','image']