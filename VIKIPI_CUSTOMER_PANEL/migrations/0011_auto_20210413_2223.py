# Generated by Django 3.1.2 on 2021-04-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIKIPI_CUSTOMER_PANEL', '0010_auto_20210410_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phnumber',
            field=models.BigIntegerField(max_length=10, null=True),
        ),
    ]