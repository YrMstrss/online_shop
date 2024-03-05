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

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs.get('product_pk'))
        cart = ShoppingCart.objects.get(user=self.request.user)

        prod = ProductInCart.objects.get_or_create(product=product, cart=cart)

        cart.total_sum = cart.total_sum - product.price * prod[0].count
        cart.save()

        prod[0].count += 1
        prod[0].summ += product.price
        cart.total_sum += prod[0].summ
        prod[0].save()
        cart.save()

        return redirect('shopping_carts:cart_view')


class RemoveFromCartAPIView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs.get('product_pk'))
        cart = ShoppingCart.objects.get(user=self.request.user)

        try:
            prod = ProductInCart.objects.get(product=product, cart=cart)

            cart.total_sum = cart.total_sum - product.price * prod.count
            cart.save()

            prod.count -= 1
            if prod.count == 0:
                prod.delete()
            else:
                prod.summ -= product.price
                cart.total_sum += prod.summ
                prod.save()
                cart.save()
        except ProductInCart.DoesNotExist:
            return redirect('shopping_carts:cart_view')

        return redirect('shopping_carts:cart_view')


class CleanCartAPIView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        cart = ShoppingCart.objects.get(user=self.request.user)
        all_products = cart.productincart_set.all()
        for product in all_products:
            product.delete()
        cart.total_sum = 0

        return redirect('shopping_carts:cart_view')
