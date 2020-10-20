from django.db import models
from django.db.models import Sum
from games.models import Game, Console
from django.conf import settings
import uuid
from django_countries.fields import CountryField


class Discounts(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)
    expiry_date = models.DateField(auto_now=False)
    offer_discount = models.DecimalField(
        max_digits=2, decimal_places=0, null=False, blank=False)
    offer_details = models.CharField(max_length=254, null=False, blank=False)
    games_or_consoles_valid = models.JSONField()


# Taken from CI Ecommerce project - edited
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, blank=True)
    county = models.CharField(max_length=80, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_total = models.DecimalField(max_digits=10, decimal_places=2,
                                         null=True, blank=True)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.original_total = self.lineitems.aggregate(Sum('lineitem_total'))[
            'lineitem_total__sum'] or 0
        if self.lineitems.total_after_discount:
            self.order_total = self.lineitems.aggregate(Sum('total_after_discount'))[
                'total_after_discount__sum'] or 0
        else:
            self.order_total = self.original_total
        if self.delivery_cost < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.original_total * \
                settings.STANDARD_DELIVERY_PERCENTAGE/100
        else:
            self.delivery_cost = 0
        self.grand_total = self.delivery_cost + self.order_total
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='lineitems')
    game = models.ForeignKey(
        Game, null=False, blank=False, on_delete=models.CASCADE)
    game_console = models.ForeignKey(
        Console, null=False, blank=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    discount = models.ForeignKey(
        Discounts, null=True, blank=True, on_delete=models.SET_NULL),
    total_after_discount = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.quantity * self.game.price
        if self.discount:
            self.total_after_discount = self.lineitem_total * \
                round(1 - self.discount.offer_discount/100)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
