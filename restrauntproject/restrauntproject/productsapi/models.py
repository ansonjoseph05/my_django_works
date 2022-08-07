from django.db import models

# Create your models here.

class Products(models.Model):
    product_name=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    category=models.CharField(max_length=120)
    rating=models.FloatField()

    def __str__(self):
        return self.product_name

