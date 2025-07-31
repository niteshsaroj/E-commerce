from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem,Category
from django.contrib.auth.decorators import login_required
from shop.models import Product
from Order.models import OrderItem
from reviews.forms import ReviewForm
from django.contrib import messages


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def product_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories,
        'query': query,
        'selected_category': category_id
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all().order_by('-created_at')
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    can_review = False
    has_reviewed = False

    if request.user.is_authenticated:
        has_reviewed = product.reviews.filter(user=request.user).exists()

        # Check if user has bought and received the product
        delivered_order_items = OrderItem.objects.filter(
            order__user=request.user,
            order__status="Delivered",
            product=product
        ).exists()

        if delivered_order_items and not has_reviewed:
            can_review = True

    if request.method == "POST" and can_review:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form,
        'can_review': can_review,
        'has_reviewed': has_reviewed,
        'related_products': related_products,
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # ✅ Check stock availability
    if product.stock <= 0:
        messages.error(request, "This product is out of stock.")
        return redirect('product_detail', product_id=product.id)

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if cart_item.quantity < product.stock:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"{product.name} added to your cart.")
    else:
        messages.warning(request, f"Only {product.stock} items in stock.")

    return redirect('product_detail', product_id=product.id)


@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', {'cart': cart})


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('view_cart')


@login_required
def increase_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.quantity += 1
    item.save()
    return redirect('view_cart')

@login_required
def decrease_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('view_cart')