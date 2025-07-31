from django.urls import path
from .views import ContactAPIView
from .views_ui import contact_view

urlpatterns = [
    path('api/', ContactAPIView.as_view(), name='contact_api'),
    path('contact/',contact_view,name='contact')
]