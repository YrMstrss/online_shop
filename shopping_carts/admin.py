from django.contrib import admin

from shopping_carts.models import ShoppingCart


@admin.register(ShoppingCart)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')
