from django.db import models
from django.conf import settings


class Promocode(models.Model):
    string_representation = models.CharField(max_length=100)
    discount_percentage = models.IntegerField()
    discount_absolute = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activation_count = models.IntegerField(default=0)
    max_activation_count = models.IntegerField(default=1)
    active_status = models.BooleanField(default=True)
    active_until_date = models.DateField()

    def __str__(self):
        return self.string_representation
