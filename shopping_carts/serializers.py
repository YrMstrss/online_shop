from rest_framework import serializers

from products.serializers import ProductSerializer
from shopping_carts.models import ShoppingCart, ProductInCart


class ProductInCartSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    summ = serializers.SerializerMethodField()

    class Meta:
        model = ProductInCart
        fields = ('product', 'count', 'summ')

    def get_summ(self, obj):
        return obj.product.price * obj.count


class ShoppingCartSerializer(serializers.ModelSerializer):

    products = ProductInCartSerializer(source='productincart_set', many=True)
    total_sum = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = '__all__'

    def get_total_sum(self, obj):
        total_summ = 0
        for product in obj.productincart_set.all():
            total_summ += product.product.price * product.count
        return total_summ
