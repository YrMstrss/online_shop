from django.db import models

from categories.models import Subcategory


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    slug = models.SlugField(max_length=100, verbose_name='slug')
    image = models.ImageField(upload_to=f'images/products/')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='подкатегория')

    def __str__(self):
        return f'{self.name} {self.price} руб.'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
