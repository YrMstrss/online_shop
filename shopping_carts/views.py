from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.response import Response

from products.models import Product
from shopping_carts.models import ShoppingCart, ProductInCart
from shopping_carts.serializers import ShoppingCartSerializer, ProductInCartUpdateSerializer
from shopping_carts.services import get_total_sum


class CartRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для вывода корзины пользователя
    """
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects.all()

    def get_object(self):
        """
        Получение корзины текущего пользователя
        :return: ShoppingCart: Корзина текущего пользователя
        """
        return ShoppingCart.objects.get(user=self.request.user)


class AddToCartAPIView(generics.GenericAPIView):
    """
    Контроллер для добавления 1 единицы товара в корзину
    """
    def get(self, request, *args, **kwargs):
        """
        Получает товар по слагу из url. В случае отсутствия данного товара в корзине создает объект ProductInCart,
        если такой товар в корзине уже есть, то добавляет 1 единицу к счетчику данного товара в корзине. А так же
        изменяет стоимость всех товаров и стоимость данного товара в корзине
        :param request:
        :param args: Позиционные аргументы
        :param kwargs: Именованные аргументы
        :return: Редирект на корзину
        """
        product = Product.objects.get(slug=kwargs.get('slug'))
        cart = ShoppingCart.objects.get(user=self.request.user)

        prod = ProductInCart.objects.get_or_create(product=product, cart=cart)
        prod[0].count += 1
        prod[0].summ += product.price
        prod[0].save()
        get_total_sum(cart)

        return redirect('shopping_carts:cart_view')


class RemoveFromCartAPIView(generics.GenericAPIView):
    """
    Контроллер для удаления 1 единицы товара из корзины
    """
    def get(self, request, *args, **kwargs):
        """
        Получает товар по слагу из url. Уменьшает количество товара в корзине на 1, если количество товаров становится
        равным нулю, удаляет товар из корзины. А так же изменяет стоимость всех товаров и стоимость данного товара в
        корзине
        :param request:
        :param args: Позиционные аргументы
        :param kwargs: Именованные аргументы
        :return: Редирект на корзину
        """
        product = Product.objects.get(slug=kwargs.get('slug'))
        cart = ShoppingCart.objects.get(user=self.request.user)

        try:
            prod = ProductInCart.objects.get(product=product, cart=cart)

            prod.count -= 1
            if prod.count == 0:
                prod.delete()
            else:
                prod.summ -= product.price
                prod.save()
            get_total_sum(cart)
        except ProductInCart.DoesNotExist:
            return redirect('shopping_carts:cart_view')

        return redirect('shopping_carts:cart_view')


class CleanCartAPIView(generics.GenericAPIView):
    """
    Контроллер для удаления всех товаров из корзины
    """
    def get(self, request, *args, **kwargs):
        """
        Удаляет все товары из корзины и устанавливает всю стоимость на 0
        :param request:
        :param args: Позиционные аргументы
        :param kwargs: Именованные аргументы
        :return: Редирект на корзину
        """
        cart = ShoppingCart.objects.get(user=self.request.user)
        cart.productincart_set.all().delete()
        cart.total_sum = 0
        cart.save()

        return redirect('shopping_carts:cart_view')


class ProductInCartDestroyAPIVIew(generics.DestroyAPIView):
    """
    Контроллер для удаления товара из корзины вне зависимости от количества
    """

    def destroy(self, request, *args, **kwargs):
        cart = ShoppingCart.objects.get(user=self.request.user)
        product = Product.objects.get(slug=kwargs.get('slug'))

        instance = ProductInCart.objects.get(product=product, cart=cart)
        self.perform_destroy(instance)
        get_total_sum(cart)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductInCartUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для обновления количества товара в корзине
    """
    serializer_class = ProductInCartUpdateSerializer

    def update(self, request, *args, **kwargs):
        cart = ShoppingCart.objects.get(user=self.request.user)
        product = Product.objects.get(slug=kwargs.get('slug'))

        partial = kwargs.pop('partial', False)
        instance = ProductInCart.objects.get(product=product, cart=cart)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        instance.summ = instance.product.price * instance.count
        instance.save()
        get_total_sum(cart)

        return Response(serializer.data)

