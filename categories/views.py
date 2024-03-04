from rest_framework import generics

from categories.models import Category
from categories.paginators import CategoryPaginator
from categories.serializers import CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPaginator
