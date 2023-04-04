from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=255)


class RoubleRate(models.Model):
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE)
    rate = models.FloatField()
