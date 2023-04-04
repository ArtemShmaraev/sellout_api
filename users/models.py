from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Your custom fields and methods here

    class Meta:
        # Set a custom related name for the 'groups' field
        # This will prevent the clash with the built-in 'auth.User.groups' field
        # and allow you to access the groups related to a user via 'my_user.my_groups.all()'
        # instead of 'my_user.groups.all()'
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    my_groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Groups',
        blank=True,
        related_name='my_users'
    )

    address = models.ManyToManyField("shipping.AddressInfo")
    all_purchase_amount = models.IntegerField(default=0)
    personal_discount_percentage = models.IntegerField(default=0)
    wishlist = models.ManyToManyField("wishlist.Wishlist", related_name='users')
    referral_link = models.CharField(max_length=100, blank=True)
    ref_user = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    preferred_size_grid = models.CharField(max_length=100, blank=True)
    last_viewed_products = models.ManyToManyField("products.Product", related_name='users_viewed', blank=True)


class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
