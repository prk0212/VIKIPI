# Generated by Django 3.1.7 on 2021-05-05 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VIKIPI_CUSTOMER_PANEL', '0017_auto_20210501_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_details',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order_details',
            name='payment_mode',
        ),
    ]
