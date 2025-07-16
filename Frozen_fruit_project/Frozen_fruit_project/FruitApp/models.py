from django.db import models
from django.forms import CharField


# Create your models here.

class Fruit(models.Model):
    name=models.CharField(max_length=100)
    price_per_kg=models.DecimalField(max_digits=6,decimal_places=2)
    quantity_in_kg=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField()
    image =models.ImageField(upload_to='fruit_images/',blank=True,null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    fruit=models.ForeignKey(Fruit,on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    quantity_ordered=models.DecimalField(max_digits=6,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name}-{self.fruit.name}"



