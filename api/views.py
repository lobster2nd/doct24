from rest_framework import generics
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class ApiViewPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 100


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.prefetch_related('subcategories')
    serializer_class = CategorySerializer
    pagination_class = ApiViewPagination


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ApiViewPagination
