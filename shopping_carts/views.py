from django.shortcuts import redirect
from rest_framework import generics

from products.models import Product
from shopping_carts.models import ShoppingCart, ProductInCart
from shopping_carts.serializers import ShoppingCartSerializer, ProductInCartSerializer


class CartRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects.all()

    def get_object(self):
        return ShoppingCart.objects.get(user=self.request.user)


class AddToCartAPIView(generics.GenericAPIView):
    serializer_class = ProductInCartSerializer

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs.get('product_pk'))
        cart = ShoppingCart.objects.get(user=self.request.user)

        prod = ProductInCart.objects.get_or_create(product=product, cart=cart)
        prod[0].count += 1
        prod[0].save()

        return redirect('shopping_carts:cart_view')
