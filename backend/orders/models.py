from django.db import models
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.

class DeliverySlot(models.Model):
    slot = models.CharField(max_length=50)      # Morning / Afternoon / Evening

    def __str__(self):
        return self.slot



class Order(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Packed", "Packed"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(DeliverySlot, on_delete=models.SET_NULL, null=True)
    total_price = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.user.username}"

    def total_price(self):
        return sum(item.total_price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_order = models.FloatField()

    def __str__(self):
        total = self.price_at_order * self.quantity
        return f"{self.product.name} x {self.quantity} = {total}"


    @property
    def total_price(self):
        return self.price_at_order * self.quantity