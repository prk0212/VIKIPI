# Generated by Django 3.1.7 on 2021-05-01 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIKIPI_CUSTOMER_PANEL', '0016_product_cart_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='ord_deliver_otp',
            field=models.IntegerField(default=7894),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order_details',
            name='payment_status',
            field=models.CharField(default='Panding', max_length=50),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
