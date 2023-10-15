from django.contrib import admin
from .models import User, Product, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'customer']
    ordering = ['-date_order']
    list_filter = ['date_order', 'total_price']


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
