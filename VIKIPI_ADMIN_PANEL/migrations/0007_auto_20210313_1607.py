# Generated by Django 3.1.7 on 2021-03-13 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIKIPI_ADMIN_PANEL', '0006_auto_20210311_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phnumber',
            field=models.IntegerField(max_length=10),
        ),
    ]
