from django.contrib import admin
from .models import OrderChangeLog

@admin.register(OrderChangeLog)
class OrderChangeLogAdmin(admin.ModelAdmin):
    list_display = ['order', 'changed_by', 'changed_at']
    readonly_fields = ['order', 'changed_by', 'changed_at', 'change_description']