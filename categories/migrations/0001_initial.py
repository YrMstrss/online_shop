# Generated by Django 5.0.3 on 2024-03-04 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('slug', models.CharField(max_length=75, verbose_name='slug')),
                ('image', models.ImageField(upload_to='images/categories')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('slug', models.CharField(max_length=75, verbose_name='slug')),
                ('image', models.ImageField(upload_to='images/categories')),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category', verbose_name='родительская категория')),
            ],
            options={
                'verbose_name': 'подкатегория',
                'verbose_name_plural': 'подкатегории',
            },
        ),
    ]
