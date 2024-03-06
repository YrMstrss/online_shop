from rest_framework import serializers

from categories.models import Subcategory, Category


class SubcategorySerializer(serializers.ModelSerializer):
    """
    Сериалайзер подкатегорий
    """
    class Meta:
        model = Subcategory
        fields = ('name', 'image')


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериалайзер категорий
    """
    subcategories = SubcategorySerializer(source='subcategory_set', many=True)

    class Meta:
        model = Category
        fields = ('name', 'image', 'subcategories')
