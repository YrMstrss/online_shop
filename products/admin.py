from django.contrib import admin

from categories.models import Category, Subcategory
from products.models import Product


@admin.display(description='Категория')
def category(obj):
    """
    Вывод в админке дополнительного поля 'категория' для модели продукта
    """
    parent_category = Subcategory.objects.get(id=obj.subcategory.id).parent_category
    return Category.objects.get(id=parent_category.id)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Регистрация модели продукта в админке
    """
    list_display = ('pk', 'name', 'price', 'subcategory', category)
    prepopulated_fields = {'slug': ('name',)}
