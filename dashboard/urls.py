# dashboard/urls.py
from django.urls import path
from .views import admin_dashboard,delete_product,add_product,edit_product,my_account

urlpatterns = [
    path('', admin_dashboard, name='admin_dashboard'),
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),
    path('dashboard/edit-product/<int:product_id>/', edit_product, name='edit_product'),
    path('add-product/', add_product, name='add_product'),
    path('account/', my_account, name='my_account'),
]
