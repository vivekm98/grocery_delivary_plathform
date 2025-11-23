from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Poster(models.Model):
    image = models.ImageField(upload_to='posters/')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        posters = Poster.objects.all().order_by('-created_at')
        if posters.count() > 3:
            for poster in posters[3:]:
                poster.image.delete()
                poster.delete()

class Unit(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
