# wishlist/views.py
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from shop.models import Product
from .models import Wishlist

@login_required
def toggle_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
    else:
        wishlist.products.add(product)

    return redirect('product_list')  # Or redirect back to product detail

@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist})
