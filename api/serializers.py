from rest_framework import serializers
from .models import Category, Subcategory, User, Cart


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('name', 'slug', 'image')


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'image', 'subcategories')



