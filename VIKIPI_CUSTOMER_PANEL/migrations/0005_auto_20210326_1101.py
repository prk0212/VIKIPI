# Generated by Django 3.1.7 on 2021-03-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIKIPI_CUSTOMER_PANEL', '0004_remove_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phnumber',
            field=models.IntegerField(max_length=10),
        ),
    ]