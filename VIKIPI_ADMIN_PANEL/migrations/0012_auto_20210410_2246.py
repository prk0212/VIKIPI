# Generated by Django 3.1.4 on 2021-04-10 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('VIKIPI_ADMIN_PANEL', '0011_auto_20210410_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phnumber', models.IntegerField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('qualification', models.CharField(default='select', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField(max_length=6)),
                ('product_quantity', models.CharField(max_length=50)),
                ('product_description', models.CharField(max_length=4000)),
                ('product_image', models.FileField(default='AdminLTELogo.png', upload_to='images/')),
                ('view', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('phnumber', models.IntegerField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('status', models.CharField(default='Pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_pic', models.FileField(default='AdminLTELogo.png', upload_to='images/')),
                ('home_country', models.CharField(max_length=30)),
                ('home_state', models.CharField(max_length=50)),
                ('home_city', models.CharField(max_length=50)),
                ('home_pincode', models.IntegerField(blank=True, max_length=10, null=True)),
                ('home_address', models.CharField(max_length=100)),
                ('otp', models.IntegerField(default=7894, max_length=8)),
                ('view', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='shop_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=200)),
                ('shop_type', models.CharField(max_length=200)),
                ('shop_country', models.CharField(max_length=30)),
                ('shop_state', models.CharField(max_length=50)),
                ('shop_city', models.CharField(max_length=50)),
                ('shop_pincode', models.IntegerField(blank=True, max_length=10, null=True)),
                ('shop_address', models.CharField(max_length=100)),
                ('view', models.BooleanField(default=False)),
                ('owner_id_proof', models.FileField(upload_to='images/')),
                ('elc_bill', models.FileField(upload_to='images/')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_ADMIN_PANEL.retailer')),
            ],
        ),
        migrations.CreateModel(
            name='retailer_FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=1000)),
                ('overall_experience', models.CharField(max_length=20)),
                ('timely_response', models.CharField(max_length=30)),
                ('our_support', models.CharField(max_length=30)),
                ('overall_setisfaction', models.CharField(max_length=30)),
                ('suggestion', models.CharField(blank=True, max_length=1000)),
                ('view', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('retailer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_ADMIN_PANEL.retailer')),
            ],
        ),
        migrations.CreateModel(
            name='product_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_image', models.FileField(upload_to='images/')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_ADMIN_PANEL.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_ADMIN_PANEL.retailer'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VIKIPI_ADMIN_PANEL.category'),
        ),
    ]