from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    slug = models.CharField(max_length=75, verbose_name='slug')
    image = models.ImageField(upload_to='images/categories')

    def __str__(self):
        return f'Категория {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    slug = models.CharField(max_length=75, verbose_name='slug')
    image = models.ImageField(upload_to='images/categories')
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='родительская категория')

    def __str__(self):
        return f'Подкатегория {self.name}'

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'
