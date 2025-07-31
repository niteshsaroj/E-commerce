from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseNotFound

def fake_admin_view(request):
    return HttpResponseNotFound("Page not found")


urlpatterns = [
    path("admin/", fake_admin_view),
    path("secret-admin-123/", admin.site.urls),
    path('',include('users.urls')),
    path('shop/',include('shop.urls')),
    path('checkout/',include('Order.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('wishlist/',include('wishlist.urls')),
    path('reviews/',include('reviews.urls')),
    path('contact/',include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)