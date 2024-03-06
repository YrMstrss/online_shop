from rest_framework import generics

from categories.models import Category
from categories.paginators import CategoryPaginator
from categories.serializers import CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка категорий
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPaginator
