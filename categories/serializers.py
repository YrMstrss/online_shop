from rest_framework import serializers

from categories.models import Subcategory, Category


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ('name', 'image')


class CategorySerializer(serializers.ModelSerializer):

    subcategories = SubcategorySerializer(source='subcategory_set', many=True)

    class Meta:
        model = Category
        fields = ('name', 'image', 'subcategories')
