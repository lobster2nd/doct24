from rest_framework import serializers
from .models import Category, Subcategory, Product, User, Cart


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'image', 'subcategories')


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Subcategory
        fields = ('name', 'slug', 'image', 'category')


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='cat.category.name')
    subcategory = serializers.CharField(source='cat.name')

    class Meta:
        model = Product
        fields = ('name', 'slug', 'price', 'image', 'category', 'subcategory')


