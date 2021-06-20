from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import *
# from .models import *


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

    stock_below_5_products = []
    for product in products:
        if product.product_quantity <= 5:
            stock_below_5_products.append(product)

    stock_below_5_prod_count = len(stock_below_5_products)

    stocked_out_products = []
    for product in products:
        if product.stocked_out():
            stocked_out_products.append(product)

    stocked_out_prod_count = len(stocked_out_products)

    hidden_disabled_products = []
    for product in products:
        if product.is_hidden() or product.disabled():
            hidden_disabled_products.append(product)

    hidden_disabled_prod_count = len(hidden_disabled_products)

    context = {'product_count': product_count,
               'stocked_out_prod_count': stocked_out_prod_count,
               'stock_below_5_prod_count': stock_below_5_prod_count,
               'stock_below_5_products': stock_below_5_products,
               'hidden_disabled_prod_count': hidden_disabled_prod_count,
               'seller': seller,
               }

    return render(request, template_name, context)


def CompanyDetailView(request):
    template_name = 'seller/form.html'
    previous_url = request.META.get('HTTP_REFERER')

    form_title = 'Sell on Medsbuy'
    form_heading = 'Company Details'
    form_button_text = 'Submit'

    user = request.user

    if hasattr(user, 'CompanyDetails'):
        form = CompanyDetailsForm(instance=user.CompanyDetails)
    else:
        form = CompanyDetailsForm()

    if request.method == 'POST':
        if hasattr(user, 'CompanyDetails'):
            form = CompanyDetailsForm(instance=user.CompanyDetails)
        else:
            form = CompanyDetailsForm()

        if form.is_valid():
            details = form.save(commit=False)
            details.seller = user
            details.save()

            return redirect('/seller/')

    context = {'form': form,
               'form_title': form_title,
               'form_heading': form_heading,
               'form_button_text': form_button_text,
               'previous_url': previous_url,
               }

    return render(request, template_name, context)


def BankDetailView(request):
    template_name = 'seller/form.html'
    previous_url = request.META.get('HTTP_REFERER')

    form_title = 'Sell on Medsbuy'
    form_heading = 'Bank Details'
    form_button_text = 'Submit'

    user = request.user

    if hasattr(user, 'BankDetails'):
        form = BankDetailsForm(instance=user.BankDetails)
    else:
        form = BankDetailsForm()

    if request.method == 'POST':
        if hasattr(user, 'BankDetails'):
            form = BankDetailsForm(instance=user.BankDetails)
        else:
            form = BankDetailsForm()

        if form.is_valid():
            details = form.save(commit=False)
            details.seller = user
            details.save()

            return redirect('/seller/')

    context = {'form': form,
               'form_title': form_title,
               'form_heading': form_heading,
               'form_button_text': form_button_text,
               'previous_url': previous_url,
               }

    return render(request, template_name, context)


def BusinessDetailView(request):
    template_name = 'seller/form.html'
    previous_url = request.META.get('HTTP_REFERER')

    form_title = 'Sell on Medsbuy'
    form_heading = 'Business Details'
    form_button_text = 'Submit'

    user = request.user

    if hasattr(user, 'BusinessDetails'):
        form = BusinessDetailsForm(instance=user.BusinessDetails)
    else:
        form = BusinessDetailsForm()

    if request.method == 'POST':
        if hasattr(user, 'BusinessDetails'):
            form = BusinessDetailsForm(instance=user.BusinessDetails)
        else:
            form = BusinessDetailsForm()

        if form.is_valid():
            details = form.save(commit=False)
            details.seller = user
            details.save()

            return redirect('/seller/')

    context = {'form': form,
               'form_title': form_title,
               'form_heading': form_heading,
               'form_button_text': form_button_text,
               'previous_url': previous_url,
               }

    return render(request, template_name, context)


@login_required(login_url='login')
def ProductsView(request):
    template_name = 'seller/listing.html'
    seller = request.user
    products = seller.products.all()
    # products = Products.objects.all()

    context = {'products': products,
               }

    return render(request, template_name, context)


def AddProductView(request):
    template_name = 'seller/form.html'
    previous_url = request.META.get('HTTP_REFERER')

    form_title = 'Sell on Medsbuy'
    form_heading = 'Add New Product'
    form_button_text = 'Add Product'

    form = AddProductForm()

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        form.instance.seller = request.user
        if form.is_valid():

            form.save()

            return redirect('/seller/products')

    context = {'form': form,
               'form_title': form_title,
               'form_heading': form_heading,
               'form_button_text': form_button_text,
               'previous_url': previous_url,
               }

    return render(request, template_name, context)


def UpdateProductView(request, pk):
    template_name = 'seller/form.html'
    previous_url = request.META.get('HTTP_REFERER')

    form_title = 'Sell on Medsbuy'
    form_heading = 'Edit Product'
    form_button_text = 'Update'

    product = request.user.products.get(pk=pk)

    form = AddProductForm(instance=product)

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES,
                              instance=product)
        # form.instance.seller = request.user
        if form.is_valid():

            form.save()

            return redirect('/seller/products')

    context = {'form': form,
               'form_title': form_title,
               'form_heading': form_heading,
               'form_button_text': form_button_text,
               'previous_url': previous_url,
               }

    return render(request, template_name, context)


def DeleteProductView(request, pk):
    template_name = 'seller/form.html'
    previous_url = request.META.get('HTTP_REFERER')

    form_title = 'Sell on Medsbuy'
    form_heading = 'Delete Product'
    form_button_text = 'Confirm Delete'

    product = request.user.products.get(pk=pk)

    heading_text = "Are you sure to delete product '" + product.product_name + "' ?"

    if request.method == 'POST':
        product.delete()

        return redirect('/seller/products')

    context = {'form_title': form_title,
               'form_heading': form_heading,
               'form_button_text': form_button_text,
               'heading_text': heading_text,
               'previous_url': previous_url,
               }

    return render(request, template_name, context)
