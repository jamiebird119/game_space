from games.models import Game, Console
from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal
from checkout.models import Discount


def bag_contents(request):
    discount = request.session.get('discount', {})
    bag_items = []
    total = 0
    total_with_discount = 0
    product_count = 0
    bag = request.session.get('bag', {})
    if discount:
        discount = get_object_or_404(Discount, pk=discount)
        for game_id in bag:
            game = get_object_or_404(Game, pk=game_id)
            for console_id, quantity in bag[game_id]['console_quantity'].items():
                console = get_object_or_404(Console, pk=console_id)
                if console.name in discount.games_or_consoles_valid.values() or game.name in discount.games_or_consoles_valid.values():
                    total += game.price * quantity
                    discount_price = game.price * \
                        (1 - discount.offer_discount/100)
                    total_with_discount += discount_price * quantity
                    product_count += quantity
                    bag_items.append({
                        'game_id': game_id,
                        'game': game,
                        'console': console,
                        'quantity': quantity,
                        'discount': discount,
                        'discount_price': discount_price
                    })
                else:
                    total += game.price * quantity
                    total_with_discount += game.price * quantity
                    product_count += quantity
                    bag_items.append({
                        'game_id': game_id,
                        'game': game,
                        'console': console,
                        'quantity': quantity,
                    })
    else:
        for game_id in bag:
            game = get_object_or_404(Game, pk=game_id)
            for console_id, quantity in bag[game_id]['console_quantity'].items():
                console = get_object_or_404(Console, pk=console_id)
                total += game.price * quantity
                product_count += quantity
                bag_items.append({
                    'game_id': game_id,
                    'game': game,
                    'console': console,
                    'quantity': quantity,
                })

        # Taken from CI Ecommerce project
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    if discount:
        grand_total = total + delivery
        discount_total = total_with_discount + delivery
        context = {
            'bag_items': bag_items,
            'total': total,
            'total_with_discount': total_with_discount,
            'discount': discount,
            'product_count': product_count,
            'free_delivery_delta': free_delivery_delta,
            'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
            'delivery': delivery,
            'discount_total': discount_total,
            'grand_total': grand_total
        }
    else:
        grand_total = total + delivery
        context = {
            'bag_items': bag_items,
            'total': total,
            'product_count': product_count,
            'free_delivery_delta': free_delivery_delta,
            'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
            'delivery': delivery,
            'grand_total': grand_total
        }

    return context
