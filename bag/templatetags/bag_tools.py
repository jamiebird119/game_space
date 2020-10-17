from django import template


register = template.Library()


# Taken from CI Ecommerce project
@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    return price * quantity
