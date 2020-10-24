from django.shortcuts import render, redirect, reverse
from .forms import OrderForm
from django.contrib import messages
from django.conf import settings
from .models import Discount
from bag.contexts import bag_contents

import stripe
# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "Sorry there is nothing in your bag.")
        return redirect(reverse("games"))

    current_bag = bag_contents(request)
    if current_bag["discount_total"]:
        total = current_bag["discount_total"]
    else:
        total = current_bag["grand_total"]
    stripe_total = round(total*100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    order_form = OrderForm
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'client_secret': settings.STRIPE_SECRET_KEY,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, template, context)


def get_discount(request):
    discount_code = request.POST.get('discount-code')
    discount = Discount.objects.all()
    redirect_url = request.POST.get('redirect_url')
    for thing in discount:
        if thing.code == discount_code:
            request.session['discount'] = discount_code
            messages.success(
                request, f'Successfully applied discount code: {discount_code}')
        else:
            messages.error(
                request, f'Could not find discount_code: {discount_code}. Please check spelling and try again.')
    return redirect(redirect_url)
