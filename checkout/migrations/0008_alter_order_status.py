# Generated by Django 3.2 on 2022-11-11 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Payment Approved', 'Payment Approved'), ('Order printed', 'Order printed'), ('Order picked', 'Order picked'), ('Order packed', 'Order packed'), ('Order shipped', 'Order shipped'), ('Order delivered', 'Order delivered')], default='Payment Approved', max_length=25),
        ),
    ]
