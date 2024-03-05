from django.urls import path

from shopping_carts.apps import ShoppingCartsConfig
from shopping_carts.views import CartRetrieveAPIView

app_name = ShoppingCartsConfig.name

urlpatterns = [
    path('', CartRetrieveAPIView.as_view(), name='cart_view'),
]
