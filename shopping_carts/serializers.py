from rest_framework import serializers

from products.serializers import ProductSerializer
from shopping_carts.models import ShoppingCart, ProductInCart


class ProductInCartSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = ProductInCart
        fields = ('product', 'count', 'summ')


class ShoppingCartSerializer(serializers.ModelSerializer):

    products = ProductInCartSerializer(source='productincart_set', many=True)

    class Meta:
        model = ShoppingCart
        fields = '__all__'


class ProductInCartUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInCart
        fields = ('count', )
