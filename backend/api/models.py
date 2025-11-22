from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ('fruits', 'Fruits'),
    ('vegetables', 'Vegetables'),
    ('dairy', 'Dairy'),
    ('household', 'Household'),
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    unit = models.CharField(max_length=20)       # kg, litre, piece, etc.
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.URLField(blank=True)          # Simple URL for beginners

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} → {self.product.name}"



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
        return f"Order {self.id} - {self.user.username}"