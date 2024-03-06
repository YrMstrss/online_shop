from rest_framework import serializers

from categories.models import Subcategory, Category
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериалайзер продукта
    """
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'image', 'slug', 'category', 'subcategory', 'price')

    def get_category(self, obj):
        """
        Получение поля 'категория' для продукта
        :param obj: Объект модели Product
        :return: str: Категория товара
        """
        parent_category = Subcategory.objects.get(id=obj.subcategory.id).parent_category
        return Category.objects.get(id=parent_category.id).name

    def get_subcategory(self, obj):
        """
        Получение название подкатегории вместо pk
        :param obj: Объект модели Product
        :return: Имя подкатегории
        """
        return Subcategory.objects.get(id=obj.subcategory.id).name
