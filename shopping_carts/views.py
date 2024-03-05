from rest_framework import generics

from shopping_carts.models import ShoppingCart, ProductInCart
from shopping_carts.serializers import ShoppingCartSerializer


class CartRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects.all()

    def get_object(self):
        return ShoppingCart.objects.get(user=self.request.user)
