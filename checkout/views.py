from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import OrderForm
from django.contrib import messages
from django.conf import settings
from .models import Discount, OrderLineItem, Order
from bag.contexts import bag_contents
from games.models import Game
import json

import stripe
# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag_info = bag_contents(request)
    if request.POST:
        bag = request.session.get("bag", {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = bag_info['bag_items']
            order.save()
            for item in bag_info['bag_items']:
                try:
                    game = get_object_or_404(Game, pk=item['game_id'])
                    console = item['console']
                    quantity = item['quantity']
                    line_item_total = item['game'].price * quantity
                    if 'discount' in item:
                        discount = item['discount']
                        total_after_discount = item['discount_price'] * quantity
                        order_line_item = OrderLineItem(
                            order=order,
                            game=game,
                            game_console=console,
                            quantity=quantity,
                            lineitem_total=line_item_total,
                            discount=discount,
                            total_after_discount=total_after_discount
                        )
                        order_line_item.save()
                    else:
                        order_line_item = OrderLineItem(
                            order=order,
                            game=game,
                            game_console=console,
                            quantity=quantity,
                            lineitem_total=line_item_total
                        )
                        order_line_item.save()
                except Game.DoesNotExist:
                    messages.error(request, (
                        "One of the gamess in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            return redirect(reverse('checkout_success', args=[order.order_number]))
    else:
        bag = request.session.get("bag", {})
        if not bag:
            messages.error(request, "Sorry there is nothing in your bag.")
            return redirect(reverse("games"))

        current_bag = bag_contents(request)
        if "discount_total" in current_bag:
            total = current_bag["discount_total"]
        else:
            total = current_bag["grand_total"]
        stripe_total = round(total*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print(intent)
        order_form = OrderForm
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'client_secret': intent.client_secret,
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


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """

    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']
    if 'discount' in request.session:
        del request.session['discount']
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
