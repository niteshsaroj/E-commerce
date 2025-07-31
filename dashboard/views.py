# orders/views.py
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from Order.models import Order
from shop.models import Product
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from shop.models import Category
from django.contrib.auth.decorators import login_required

from django.db.models import Sum, Count
from django.utils.timezone import now
from datetime import timedelta
from collections import defaultdict

# Add in your admin_dashboard view:
from django.db.models.functions import TruncMonth


@staff_member_required
def admin_dashboard(request):
    if request.method == "POST" and 'order_id' in request.POST:
      order_id = request.POST.get("order_id")
      new_status = request.POST.get("status")
      order = Order.objects.get(id=order_id)
  
      # ✅ If order just changed to Delivered, reduce product stock
      if new_status == "Delivered" and order.status != "Delivered":
          for item in order.items.all():
              product = item.product
              product.stock = max(product.stock - item.quantity, 0)  # ensure no negative stock
              product.save()
  
      order.status = new_status
      order.save()
      return redirect('admin_dashboard')


    orders = Order.objects.all().order_by('-created_at')
    products = Product.objects.all()
    categories = Category.objects.all()
    low_stock_products = Product.objects.filter(stock__lte=5)


    total_orders = orders.count()
    total_revenue = orders.aggregate(Sum('total_price'))['total_price__sum'] or 0
    total_products = products.count()
    pending_orders = orders.filter(status='Pending').count()
    
    # Monthly sales chart
    monthly_data = orders.annotate(month=TruncMonth('created_at')).values('month').annotate(total=Sum('total_price')).order_by('month')
    sales_months = [data['month'].strftime('%b %Y') for data in monthly_data]
    sales_totals = [float(data['total']) for data in monthly_data]
    
    # Revenue by category
    category_data = Product.objects.values('category__name').annotate(revenue=Sum('orderitem__price')).order_by('-revenue')
    category_names = [item['category__name'] for item in category_data]
    category_revenue = [float(item['revenue'] or 0) for item in category_data]
   
    return render(request, 'admin_dashboard.html', {
        'orders': orders,
        'products': products,
        'categories': categories,
        'low_stock_products': low_stock_products,
        'total_orders': total_orders,
    'total_revenue': total_revenue,
    'total_products': total_products,
    'pending_orders': pending_orders,
    'sales_months': sales_months,
    'sales_totals': sales_totals,
    'category_names': category_names,
    'category_revenue': category_revenue,
    })


@staff_member_required
@require_POST
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        messages.success(request, "Product deleted.")
    except:
        messages.error(request, "Could not delete product.")
    return HttpResponseRedirect(reverse('admin_dashboard'))


@staff_member_required
@require_POST
def add_product(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    category_id = request.POST.get("category")
    image = request.FILES.get("image")

    category = Category.objects.get(id=category_id)

    Product.objects.create(
        name=name,
        description=description,
        price=price,
        stock=stock,
        category=category,
        image=image
    )

    return redirect("admin_dashboard")


@staff_member_required
def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = Category.objects.all()

    if request.method == "POST":
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")
        category_id = request.POST.get("category")
        product.category = Category.objects.get(id=category_id)

        if request.FILES.get("image"):
            product.image = request.FILES["image"]

        product.save()
        return redirect('admin_dashboard')

    return render(request, 'edit_product.html', {
        'product': product,
        'categories': categories
    })


@login_required
def my_account(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    cancelled_count = orders.filter(status='Cancelled').count()
    return render(request, 'my_account.html', {
        'orders': orders,
        'cancelled_count': cancelled_count
    })