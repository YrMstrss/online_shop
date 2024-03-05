from django.urls import path

from shopping_carts.apps import ShoppingCartsConfig
from shopping_carts.views import CartRetrieveAPIView, AddToCartAPIView, RemoveFromCartAPIView

app_name = ShoppingCartsConfig.name

urlpatterns = [
    path('', CartRetrieveAPIView.as_view(), name='cart_view'),
    path('add/<int:product_pk>/', AddToCartAPIView.as_view(), name='add_to_cart'),
    path('remove/<int:product_pk>/', RemoveFromCartAPIView.as_view(), name='remove_from_cart')
]
