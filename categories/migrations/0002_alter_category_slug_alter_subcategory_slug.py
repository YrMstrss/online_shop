# Generated by Django 5.0.3 on 2024-03-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=75, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(max_length=75, verbose_name='slug'),
        ),
    ]
