from django.contrib import admin

from shopping_carts.models import ShoppingCart, ProductInCart


@admin.register(ShoppingCart)
class CartAdmin(admin.ModelAdmin):
    """
    Регистрация в админке модели корзины
    """
    list_display = ('pk', 'user')


@admin.register(ProductInCart)
class ProductInCartAdmin(admin.ModelAdmin):
    """
    Регистрация в админке модели товара из корзины
    """
    list_display = ('pk', 'product', 'cart', 'count')
