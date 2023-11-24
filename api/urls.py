from django.urls import path
from .views import CategoryAPIView, ProductAPIView


urlpatterns = [
    path('category_list/', CategoryAPIView.as_view(), name='cat_list'),
    path('product_list/', ProductAPIView.as_view(), name='prod_list'),
]
