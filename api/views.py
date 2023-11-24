from rest_framework import generics, status
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Category, Product, Cart
from .serializers import (CategorySerializer, ProductSerializer,
                          CartSerializer, MyTokenObtainPairSerializer,
                          UserSerializer)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ApiViewPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 100


class CategoryAPIView(generics.ListAPIView):
    """View all categories and subcategories"""
    queryset = Category.objects.prefetch_related('subcategories')
    serializer_class = CategorySerializer
    pagination_class = ApiViewPagination
    permission_classes = [AllowAny]


class ProductAPIView(generics.ListAPIView):
    """View all products with category and subcategory"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ApiViewPagination
    permission_classes = [AllowAny]


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def cart_view(request):
    """Operations with current user cart"""
    if request.method == 'GET':
        """View user cart"""
        cart = Cart.objects.filter(user=request.user).first()
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        """Clear user cart"""
        cart = Cart.objects.filter(user=request.user).first()
        cart.products.clear()
        return Response(status=status.HTTP_204_NO_CONTENT)
