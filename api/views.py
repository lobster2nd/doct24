from rest_framework import generics, status
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
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


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.products.add(product, through_defaults={'quantity': quantity})

        return Response({'success': 'Product added to cart'}, status=200)


class UpdateCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, cart_item_id):
        quantity = request.data.get('quantity')

        try:
            cart_item = Cart.products.through.objects.get(id=cart_item_id, cart__user=request.user)
        except Cart.products.through.DoesNotExist:
            return Response({'error': 'Cart item not found'}, status=404)

        cart_item.quantity = quantity
        cart_item.save()

        return Response({'success': 'Cart item updated'}, status=200)


class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, cart_item_id):
        try:
            cart_item = Cart.products.through.objects.get(id=cart_item_id, cart__user=request.user)
        except Cart.products.through.DoesNotExist:
            return Response({'error': 'Cart item not found'}, status=404)

        cart_item.delete()

        return Response({'success': 'Cart item removed'}, status=200)
