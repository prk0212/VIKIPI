# Generated by Django 3.1.4 on 2021-04-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIKIPI_CUSTOMER_PANEL', '0009_auto_20210410_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phnumber',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]