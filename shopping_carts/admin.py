from django.contrib import admin

from shopping_carts.models import ShoppingCart, ProductInCart


@admin.register(ShoppingCart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')


@admin.register(ProductInCart)
class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'cart', 'count')
