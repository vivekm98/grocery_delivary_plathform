from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class DeliverySlot(models.Model):
    slot = models.CharField(max_length=50)  # Morning / Afternoon / Evening

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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    slot = models.ForeignKey(DeliverySlot, on_delete=models.SET_NULL, null=True)
    total_price = models.FloatField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_order = models.FloatField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    @property
    def total_price(self):
        return self.price_at_order * self.quantity