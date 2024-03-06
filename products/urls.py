from django.urls import path

from products.apps import ProductsConfig
from products.views import ProductListAPIView

app_name = ProductsConfig.name

urlpatterns = [
    path('list/', ProductListAPIView.as_view(), name='list-product'),
]