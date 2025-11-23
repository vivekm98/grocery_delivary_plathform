from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Subscription(models.Model):
    FREQUENCY_CHOICES = (
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    next_delivery_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.frequency})"

