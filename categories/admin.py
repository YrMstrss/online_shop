from django.contrib import admin

from categories.models import Category, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Регистрация модели категории в админке
    """
    list_display = ('pk', 'name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    """
    Регистрация модели подкатегории в админке
    """
    list_display = ('pk', 'name')
    prepopulated_fields = {'slug': ('name',)}
