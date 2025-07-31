from django.urls import path
from .views import toggle_wishlist, wishlist_view

urlpatterns = [
    path('', wishlist_view, name='wishlist'),
    path('toggle/<int:product_id>/', toggle_wishlist, name='toggle_wishlist'),
]
