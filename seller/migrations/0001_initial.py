# Generated by Django 3.2.4 on 2021-06-19 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='BankDetails', serialize=False, to='auth.user')),
                ('bank_name', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('branch', models.CharField(max_length=150)),
                ('account_holder_name', models.CharField(max_length=150)),
                ('account_number', models.IntegerField()),
                ('IFSC', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessDetails',
            fields=[
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='BusinessDetails', serialize=False, to='auth.user')),
                ('business_name', models.CharField(max_length=150)),
                ('GSTIN', models.CharField(max_length=15)),
                ('TAN', models.ImageField(upload_to='seller_details/TAN')),
                ('signature', models.ImageField(upload_to='seller_details/signature')),
                ('address_l1', models.CharField(max_length=300, verbose_name='Address Line 1')),
                ('address_l2', models.CharField(blank=True, max_length=300, null=True, verbose_name='Address Line 2')),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('business_type', models.CharField(max_length=150)),
                ('PersonalPAN', models.CharField(max_length=150)),
                ('BusinessPAN', models.CharField(max_length=150)),
                ('address_proof', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('company_name', models.CharField(max_length=150)),
                ('GSTIN', models.CharField(max_length=15)),
                ('address_l1', models.CharField(max_length=300, verbose_name='Address Line 1')),
                ('address_l2', models.CharField(blank=True, max_length=300, null=True, verbose_name='Address Line 2')),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('product_price', models.FloatField()),
                ('product_MRP', models.FloatField()),
                ('product_quantity', models.IntegerField()),
                ('product_status', models.CharField(choices=[('Active', 'Active'), ('Disabled', 'Disabled'), ('Hidden', 'Hidden'), ('Stock Out', 'Stock Out')], default='Active', max_length=100)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(blank=True, max_length=100, null=True)),
                ('order_status', models.CharField(choices=[('Hub', 'Hub'), ('Active', 'Active'), ('Returned', 'Returned'), ('Cancelled', 'Cancelled')], max_length=100)),
                ('products', models.ManyToManyField(to='seller.Products')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.orders')),
            ],
        ),
    ]
