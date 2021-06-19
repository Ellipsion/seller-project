# Generated by Django 3.2.3 on 2021-06-16 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20210616_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='order',
        ),
        migrations.AddField(
            model_name='orders',
            name='products',
            field=models.ManyToManyField(to='seller.Products'),
        ),
    ]