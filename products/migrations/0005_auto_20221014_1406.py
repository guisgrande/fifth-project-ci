# Generated by Django 3.2 on 2022-10-14 14:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20221014_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='offer_discount',
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(0)]),
        ),
    ]
