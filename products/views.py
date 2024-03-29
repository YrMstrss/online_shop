from rest_framework import generics

from products.models import Product
from products.paginators import ProductPaginator
from products.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка продуктов
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPaginator
