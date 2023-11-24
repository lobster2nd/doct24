from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Subcategory, User, Cart
from .serializers import CategorySerializer, SubcategorySerializer


class ApiViewPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 100


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.prefetch_related('subcategories')
    serializer_class = CategorySerializer
    pagination_class = ApiViewPagination
