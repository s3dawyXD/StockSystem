from django.db import models

from .utils import update_stock


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    low_stock_alert_sent = models.BooleanField(default=False)
    initial_stock = models.DecimalField(max_digits=10, decimal_places=2, default=1000)


class Product(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient, through="ProductIngredient")


class ProductIngredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)


class OrderData(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, related_name="order_data"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        update_stock(self)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ### add more fields as needed
