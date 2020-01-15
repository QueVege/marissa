from django.db import models


class Product(models.Model):
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=100)
    image = models.URLField()
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=500)

    def __str__(self):
            return self.name