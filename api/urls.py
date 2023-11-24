from django.urls import path

from .views import (CategoryAPIView, ProductAPIView, cart_view,
                    MyTokenObtainPairView, CreateUserView)

urlpatterns = [
    path('category_list/', CategoryAPIView.as_view(), name='cat_list'),
    path('product_list/', ProductAPIView.as_view(), name='prod_list'),
    path('cart/', cart_view, name='cart'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('token/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]
