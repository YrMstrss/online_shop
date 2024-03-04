from django.contrib.postgres.fields import ArrayField
from django.db import models

from products.models import Product
from users.models import User


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')
    count = models.IntegerField(default=1, verbose_name='количество в корзине')
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, verbose_name='корзина')
