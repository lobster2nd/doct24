from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView, TokenVerifyView

from .views import (CategoryAPIView, ProductAPIView, cart_view,
                    MyTokenObtainPairView, CreateUserView)

urlpatterns = [
    path('category_list/', CategoryAPIView.as_view(), name='cat_list'),
    path('product_list/', ProductAPIView.as_view(), name='prod_list'),
    path('cart/', cart_view, name='cart'),
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
