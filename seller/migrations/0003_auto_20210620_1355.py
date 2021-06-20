# Generated by Django 3.2.4 on 2021-06-20 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0002_auto_20210620_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, default=12, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businessdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, default=12, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companydetails',
            name='id',
            field=models.BigAutoField(auto_created=True, default=12, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bankdetails',
            name='seller',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='BankDetails', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='businessdetails',
            name='seller',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='BusinessDetails', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='companydetails',
            name='seller',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CompanyDetails', to=settings.AUTH_USER_MODEL),
        ),
    ]
