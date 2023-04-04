from django.db import models


class DeliveryType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Formula(models.Model):
    brand = models.ForeignKey("products.Brand", on_delete=models.CASCADE)
    delivery_type = models.ForeignKey("DeliveryType", on_delete=models.CASCADE)
    moscow_del_price = models.IntegerField()
    extra_charge_percentage = models.FloatField()
    rounding_step = models.IntegerField()

    def __str__(self):
        return f'Formula for {self.brand} ({self.delivery_type})'


class AddressInfo(models.Model):
    address = models.CharField(max_length=255)
    post_index = models.CharField(max_length=10)

    def __str__(self):
        return self.address


class Platform(models.Model):
    platform = models.CharField(max_length=255)
    site = models.CharField(max_length=10)


class UnitBundle(models.Model):
    size = models.ForeignKey("products.Size", on_delete=models.CASCADE, related_name='unit_bundles')
    orig_price = models.IntegerField()
    currency = models.ForeignKey("utils.Currency", on_delete=models.CASCADE)
    final_price = models.IntegerField()
    delivery_type = models.ForeignKey("DeliveryType", on_delete=models.CASCADE, related_name='unit_bundles')
    platform = models.ForeignKey("Platform", on_delete=models.CASCADE, related_name='unit_bundles')
    availability = models.BooleanField()


class ProductUnit(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='product_units')
    unit_bundle = models.ForeignKey("UnitBundle", on_delete=models.CASCADE, related_name='product_units')
