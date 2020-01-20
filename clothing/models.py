from django.db import models


class Product(models.Model):
    url = models.URLField(max_length=200, null=True)
    name = models.CharField(max_length=100, null=True)
    image = models.URLField(null=True)
    brand = models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=500, null=True)
    category = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name