from django.urls import path
from .views import checkout_view, my_orders_view, order_detail, cancel_order,generate_invoice,export_orders_csv,export_orders_excel



urlpatterns = [
    path('checkout/', checkout_view, name='checkout'),
    path('my-orders/', my_orders_view, name='my_orders'),
    path('<int:order_id>/', order_detail, name='order_detail'),
    path('cancel-order/<int:order_id>/', cancel_order, name='cancel_order'),
    path('<int:order_id>/invoice/', generate_invoice, name='generate_invoice'),
    path('admin/export-csv/', export_orders_csv, name='export_orders_csv'),
    path('admin/export-excel/', export_orders_excel, name='export_orders_excel'),
    
]
