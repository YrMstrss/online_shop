from rest_framework import serializers

from products.serializers import ProductSerializer
from shopping_carts.models import ShoppingCart, ProductInCart


class ProductInCartSerializer(serializers.ModelSerializer):
    """
    Сериалайзер товара в корзине
    """
    product = ProductSerializer()

    class Meta:
        model = ProductInCart
        fields = ('product', 'count', 'summ')


class ShoppingCartSerializer(serializers.ModelSerializer):
    """
    Сериалайзер корзины
    """
    products = ProductInCartSerializer(source='productincart_set', many=True)

    class Meta:
        model = ShoppingCart
        fields = '__all__'


class ProductInCartUpdateSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для обновления количества товара в корзине
    """
    class Meta:
        model = ProductInCart
        fields = ('count', )
