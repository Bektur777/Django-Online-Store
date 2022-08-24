from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'phone', 'paid', 'created')
    list_display_links = ('user',)
    search_fields = ('user', 'email',)
    list_editable = ('paid',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price')
    list_display_links = ('order',)



