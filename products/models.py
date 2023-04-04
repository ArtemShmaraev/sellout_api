from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)


class Size(models.Model):
    INT = models.CharField(max_length=15)
    US = models.CharField(max_length=15)
    UK = models.CharField(max_length=15)
    EU = models.CharField(max_length=15)
    IT = models.CharField(max_length=15)
    RU = models.CharField(max_length=15)

    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, related_name='sizes')


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Gender(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    brand = models.ManyToManyField("Brand", related_name='products')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField("Tag", related_name='products')
    bucket_link = models.CharField(max_length=255)
    sizes = models.ManyToManyField("Size", related_name='products')
    description = models.TextField()
    article = models.CharField(max_length=255)
    gender = models.ForeignKey("Gender", on_delete=models.CASCADE, related_name='products')
    available_flag = models.BooleanField()
    last_upd = models.DateTimeField()
    add_date = models.DateField()
    fit = models.IntegerField()
    rel_num = models.IntegerField()


class SizeTranslationGrid(models.Model):
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    US = models.FloatField()
    UK = models.FloatField()
    EU = models.FloatField()
    RU = models.FloatField()