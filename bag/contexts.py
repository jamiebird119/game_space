from games.models import Game, Console
from django.shortcuts import get_object_or_404


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
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count
    }
    return context
