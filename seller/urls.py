from django.urls import path, include

from . import views

app_name = 'seller'
urlpatterns = [
    path('', views.IndexView, name='new'),
    path('dashboard', views.DashboardView, name='dash'),
    path('companydetails/', views.CompanyDetailView, name='company'),
    path('bankdetails/', views.BankDetailView, name='bank'),
    path('businessdetails/', views.BusinessDetailView, name='business'),
    path('products/', views.ProductsView, name='products'),
    path('products/add/', views.AddProductView, name='add_product'),
    path('products/update/<int:pk>',
         views.UpdateProductView, name='update_product'),
    path('products/delete/<int:pk>',
         views.DeleteProductView, name='delete_product'),
]
