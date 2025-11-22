from django.contrib import admin
from .models import Cart,Product,DeliverySlot,Order
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'unit')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')

admin.site.register(Cart)
admin.site.register(Product,ProductAdmin)
admin.site.register(DeliverySlot)
admin.site.register(Order,OrderAdmin)

