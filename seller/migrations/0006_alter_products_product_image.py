# Generated by Django 3.2.4 on 2021-06-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_alter_products_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(upload_to='product_images/'),
        ),
    ]
