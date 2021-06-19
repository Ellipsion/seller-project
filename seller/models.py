from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class CompanyDetails(models.Model):
    pass


class BankDetails(models.Model):
    seller = models.OneToOneField(User, on_delete=CASCADE)

    bank_name = models.CharField(max_length=150,)
    city = models.CharField(max_length=150,)
    state = models.CharField(max_length=150,)
    branch = models.CharField(max_length=150,)

    account_holder_name = models.CharField(max_length=150,)
    account_number = models.IntegerField()
    IFSC = models.CharField(max_length=100,)

    def __str__(self):
        return self.seller.username


class BusinessDetails(models.Model):
    seller = models.OneToOneField(User, on_delete=CASCADE)

    business_name = models.CharField(max_length=150,)

    GSTIN = models.CharField(max_length=15,)
    TAN = models.ImageField()
    signature = models.ImageField()

    address_l1 = models.CharField(
        max_length=300, verbose_name='Address Line 1')
    address_l2 = models.CharField(
        max_length=300, verbose_name='Address Line 2', blank=True, null=True,)
    pincode = models.IntegerField()
    city = models.CharField(max_length=150,)
    state = models.CharField(max_length=150,)
    country = models.CharField(max_length=150,)

    business_type = models.CharField(max_length=150,)

    PersonalPAN = models.CharField(max_length=150,)
    BusinessPAN = models.CharField(max_length=150,)

    address_proof = models.ImageField()


class Products(models.Model):
    seller = models.ForeignKey(
        User, related_name='products', on_delete=CASCADE)
    # order = models.ForeignKey(
    #     Orders, related_name='products', on_delete=CASCADE)

    product_name = models.CharField(max_length=300,)
    product_image = models.ImageField(
        upload_to='product_images/',)

    product_price = models.FloatField()
    product_MRP = models.FloatField()

    product_quantity = models.IntegerField()

    STATUS = (
        ('Active', 'Active'),
        ('Disabled', 'Disabled'),
        ('Hidden', 'Hidden'),
        ('Stock Out', 'Stock Out'),
    )

    product_status = models.CharField(
        max_length=100, choices=STATUS, default='Active',)

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    seller = models.ForeignKey(User, on_delete=CASCADE)
    order_name = models.CharField(max_length=100, blank=True, null=True)
    products = models.ManyToManyField(Products,)
    STATUS = [
        ('Hub', 'Hub'),
        ('Active', 'Active'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled'),
    ]
    order_status = models.CharField(max_length=100, choices=STATUS,)

    def __str__(self):
        return self.order_name


class AdditionalDetail(models.Model):
    product = models.ForeignKey(Orders, on_delete=CASCADE)
    name = models.CharField(max_length=100,)
    description = models.CharField(max_length=300,)
