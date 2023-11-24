from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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


class CartSerializer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField()
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('user', 'products', 'total_quantity', 'total_cost')

    def get_total_quantity(self, obj):
        return obj.products.count()

    def get_total_cost(self, obj):
        return sum(product.price for product in obj.products.all())


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
