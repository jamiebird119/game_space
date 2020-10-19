from games.models import Game, Console
from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal


# Taken from code institute e commerce project
def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

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
