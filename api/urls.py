from django.urls import path
from .views import CategoryAPIView


urlpatterns = [
    path('category_list/', CategoryAPIView.as_view(), name='cat_list')
]
