from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


@login_required(login_url='login')
def IndexView(request):
    template_name = 'seller/new_user.html'

    seller = request.user
    context = {'seller': seller,
               }

    return render(request, template_name, context)


@login_required(login_url='login')
def DashboardView(request):
    template_name = 'seller/index.html'

    seller = request.user
    products = seller.products.all()
    # products = Products.objects.all()
    product_count = products.count()

    stocked_out_products = []
    for product in products:
        if product.product_quantity == 0:
            stocked_out_products.append(product)

    stocked_out_prod_count = len(stocked_out_products)

    context = {'product_count': product_count,
               'stocked_out_prod_count': stocked_out_prod_count,
               'seller': seller,
               }

    return render(request, template_name, context)


def BankDetailView(request):
    template_name = 'seller/bank_detail.html'

    form = BankDetailsForm()

    if request.method == 'POST':
        form = BankDetailsForm(request.POST)
        form.instance.seller = request.user
        if form.is_valid():
            form.save()

            return redirect('/seller/')

    context = {'form': form, }

    return render(request, template_name, context)


def CompanyDetailView(request):
    pass


def BusinessDetailView(request):
    template_name = 'seller/business_detail.html'

    form = BusinessDetailsForm()
    fields = list(form)

    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        form.instance.seller = request.user
        if form.is_valid():
            form.save()

            return redirect('/seller/')

    context = {'form': form,
               'form_fields': fields,
               }

    return render(request, template_name, context)


@login_required
def ProductsView(request):
    template_name = 'seller/listing.html'
    seller = request.user
    products = seller.products.all()
    # products = Products.objects.all()

    context = {'products': products,
               }

    return render(request, template_name, context)


def AddProductView(request):
    template_name = 'seller/add_product.html'

    form = AddProductForm()
    fields = list(form)

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        form.instance.seller = request.user
        if form.is_valid():
            # print('submitted')
            form.save()

            return redirect('/seller/products')

    context = {'form': form,
               'form_fields': fields,
               }

    return render(request, template_name, context)
