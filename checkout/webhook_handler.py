from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem, Discount
from games.models import Game, Console
from profiles.models import UserProfile

import time
import json


class StripeWH_Handler():

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200)

    def _send_confirmation_email(self, order):
        print("attempting to send email")
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {"order": order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_payment_intent_succeeded(self, event):

        intent = event.data.object
        pid = intent.id
        bag = json.loads(intent.metadata.bag)
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.charges.data[0].shipping
        grand_total = round(intent.charges.data[0].amount/100)
        if 'discount' in intent.metadata:
            discount = intent.metadata.discount
        else:
            discount = None
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_county = shipping_details.address.state
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    grand_total__iexact=grand_total,
                    stripe_pid__iexact=pid,
                    original_bag__iexact=bag
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook success recieved: {event["type"]}| SUCCESS - Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    user=profile,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    stripe_pid=pid,
                    original_bag=json.dumps(bag)
                )
                if discount:
                    discount = get_object_or_404(Discount, pk=discount)
                    for game_id in bag:
                        game = get_object_or_404(Game, pk=game_id)
                        for console_id, quantity in bag[game_id]['console_quantity'].items():
                            console = get_object_or_404(Console, pk=console_id)
                            if console.name in discount.games_or_consoles_valid.values() or game.name in discount.games_or_consoles_valid.values():
                                discount_price = game.price * \
                                    (1 - discount.offer_discount/100)
                                order_line_item = OrderLineItem(
                                    order=order,
                                    game=game,
                                    game_console=console,
                                    quantity=quantity,
                                    lineitem_total=game.price*quantity,
                                    discount=discount,
                                    total_after_discount=discount_price*quantity
                                )
                                order_line_item.save()
                            else:
                                order_line_item = OrderLineItem(
                                    order=order,
                                    game=game,
                                    game_console=console,
                                    quantity=quantity,
                                    lineitem_total=game.price*quantity,
                                )
                                order_line_item.save()
                else:
                    for game_id in bag:
                        game = get_object_or_404(Game, pk=game_id)
                        for console_id, quantity in bag[game_id]['console_quantity'].items():
                            console = get_object_or_404(Console, pk=console_id)
                            order_line_item = OrderLineItem(
                                order=order,
                                game=game,
                                game_console=console,
                                quantity=quantity,
                                lineitem_total=game.price*quantity,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                print(f'Error as: {e}')
                return HttpResponse(content=f'An error has occured: {event["type"]} | ERROR', status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook success recieved: {event["type"]} | SUCCESS Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook failure recieved: {event["type"]}',
            status=200)
