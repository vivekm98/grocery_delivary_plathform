from django.contrib import admin
from .models import DeliverySlot,Order,OrderItem
# Register your models here.
admin.site.register(DeliverySlot)
admin.site.register(Order)
admin.site.register(OrderItem)