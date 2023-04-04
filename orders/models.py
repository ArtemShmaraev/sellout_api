from django.db import models
from django.conf import settings


class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_unit = models.ForeignKey("shipping.ProductUnit", on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.ForeignKey("shipping.AddressInfo", on_delete=models.CASCADE)
    promocode = models.ForeignKey("promotions.Promocode", on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)
    fact_of_payment = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} order: {self.product_unit}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_unit = models.ForeignKey("shipping.ProductUnit", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} cart: {self.product_unit}'
