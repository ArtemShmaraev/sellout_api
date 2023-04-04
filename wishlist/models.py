from django.db import models


class Wishlist(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    size = models.ForeignKey("products.Size", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} ({self.size}) in wishlist'
