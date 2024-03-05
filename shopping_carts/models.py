from django.db import models

from products.models import Product
from users.models import User


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    total_sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='цена всех товаров')

    def __str__(self):
        return f'Корзина {self.user.username}'

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')
    count = models.IntegerField(default=0, verbose_name='количество в корзине')
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, verbose_name='корзина')
    summ = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='цена товаров')

    def __str__(self):
        return f'{self.product.name} в корзине {self.cart}'

    class Meta:
        verbose_name = 'товар в корзине'
        verbose_name_plural = 'товары в корзине'
