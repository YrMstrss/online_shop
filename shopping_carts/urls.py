from django.urls import path

from shopping_carts.apps import ShoppingCartsConfig
from shopping_carts.views import CartRetrieveAPIView, AddToCartAPIView, RemoveFromCartAPIView, CleanCartAPIView, \
    ProductInCartDestroyAPIVIew, ProductInCartUpdateAPIView

app_name = ShoppingCartsConfig.name

urlpatterns = [
    path('', CartRetrieveAPIView.as_view(), name='cart_view'),
    path('add/<slug:slug>/', AddToCartAPIView.as_view(), name='add_to_cart'),
    path('remove/<slug:slug>/', RemoveFromCartAPIView.as_view(), name='remove_from_cart'),
    path('clean/', CleanCartAPIView.as_view(), name='clean_cart'),
    path('delete/<slug:slug>/', ProductInCartDestroyAPIVIew.as_view(), name='delete_from_cart'),
    path('update/<slug:slug>/', ProductInCartUpdateAPIView.as_view(), name='update_cart'),
]
