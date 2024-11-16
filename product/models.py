from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/images')


    def __str__(self):
        return self.name
