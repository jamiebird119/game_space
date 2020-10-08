from django.db import models


# Create your models here.
class Console(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Genre(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Game(models.Model):
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254, blank=True)
    description = models.TextField(max_length=350)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genres = models.ManyToManyField('Genre', blank=True)
    consoles = models.ManyToManyField('Console', blank=True)
    rating = models.DecimalField(
        max_digits=3, decimal_places=0, null=True, blank=True)
    release_year = models.DecimalField(max_digits=4, decimal_places=0)
    publisher = models.CharField(max_length=254, blank=True)
    image_url = models.CharField(max_length=254, blank=True)
    image = models.ImageField(blank=True)
    special_offer = models.BooleanField(null=True, blank=True)
    offer_percentage = models.DecimalField(
        max_digits=3, decimal_places=0, null=True, blank=True)
    original_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
