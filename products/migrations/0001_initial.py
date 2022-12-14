# Generated by Django 3.2 on 2022-09-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sku', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[(1, 'Others'), (2, 'Skateboards'), (3, 'Bags'), (4, 'Caps')], default=1, max_length=25)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['-release_date'],
            },
        ),
    ]
