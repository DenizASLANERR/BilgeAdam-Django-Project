from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from decimal import Decimal
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

    def total_price(self):
        return Decimal(self.product.price) * int(self.quantity)
