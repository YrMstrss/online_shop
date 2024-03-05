from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.response import Response

from products.models import Product
from shopping_carts.models import ShoppingCart, ProductInCart
from shopping_carts.serializers import ShoppingCartSerializer, ProductInCartUpdateSerializer


class CartRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects.all()

    def get_object(self):
        return ShoppingCart.objects.get(user=self.request.user)


class AddToCartAPIView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(slug=kwargs.get('slug'))
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
        product = Product.objects.get(slug=kwargs.get('slug'))
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
        cart.save()

        return redirect('shopping_carts:cart_view')


class ProductInCartDestroyAPIVIew(generics.DestroyAPIView):
    def get_queryset(self):
        cart = ShoppingCart.objects.get(user=self.request.user)
        return ProductInCart.objects.filter(cart=cart)

    def get_object(self, *args, **kwargs):
        product = Product.objects.get(slug=kwargs.get('slug'))
        cart = ShoppingCart.objects.get(user=self.request.user)
        return ProductInCart.objects.get(product=product, cart=cart)

    def destroy(self, request, *args, **kwargs):
        cart = ShoppingCart.objects.get(user=self.request.user)
        instance = self.get_object(self, *args, **kwargs)
        cart.total_sum -= instance.product.price * instance.count
        cart.save()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductInCartUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductInCartUpdateSerializer

    def get_queryset(self):
        cart = ShoppingCart.objects.get(user=self.request.user)
        return ProductInCart.objects.filter(cart=cart)

    def get_object(self, *args, **kwargs):
        product = Product.objects.get(slug=kwargs.get('slug'))
        cart = ShoppingCart.objects.get(user=self.request.user)
        return ProductInCart.objects.get(product=product, cart=cart)

    def update(self, request, *args, **kwargs):
        cart = ShoppingCart.objects.get(user=self.request.user)
        partial = kwargs.pop('partial', False)
        instance = self.get_object(self, *args, **kwargs)
        cart.total_sum -= instance.summ
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        instance.summ = instance.product.price * instance.count
        instance.save()
        cart.total_sum += instance.summ
        cart.save()

        return Response(serializer.data)

