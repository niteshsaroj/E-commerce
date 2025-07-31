from django.urls import path,include
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import ProductViewSet, CategoryViewSet
from .views_ui import product_list, product_detail ,add_to_cart, view_cart, remove_from_cart, increase_cart_item,decrease_cart_item
from rest_framework.routers import DefaultRouter
from Order.api_views import OrderViewSet
from reviews.views import ReviewViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="E-Commerce API",
      default_version='v1',
      description="API for e-commerce app with JWT",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[],
)

router = DefaultRouter()
router.register('categories',CategoryViewSet)
router.register('prodcuts',ProductViewSet)
router.register('orders', OrderViewSet)
router.register('reviews', ReviewViewSet)


handler404 = 'shop.views.custom_404'


urlpatterns=[
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/increase/<int:item_id>/', increase_cart_item, name='increase_cart_item'),
    path('cart/decrease/<int:item_id>/', decrease_cart_item, name='decrease_cart_item'),
]

if settings.DEBUG:
    urlpatterns += [
        path("docs/", schema_view.with_ui('swagger', cache_timeout=0)),
    ]