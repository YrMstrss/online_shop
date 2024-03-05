from django.urls import path

from shopping_carts.apps import ShoppingCartsConfig
from shopping_carts.views import CartRetrieveAPIView, AddToCartAPIView

app_name = ShoppingCartsConfig.name

urlpatterns = [
    path('', CartRetrieveAPIView.as_view(), name='cart_view'),
    path('add/<int:product_pk>/', AddToCartAPIView.as_view(), name='add_to_cart')
]
