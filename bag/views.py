from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from django.contrib import messages
from games.models import Game, Console
# Create your views here.


def get_bag(request):
    template = 'bag/bag.html'
    context = {
    }
    return render(request, template, context)


def add_to_bag(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    console_id = request.POST.get('console')
    console = get_object_or_404(Console, pk=console_id)
    bag = request.session.get('bag', {})
    if game_id in list(bag.keys()):
        if console_id in bag[game_id]['console_quantity'].keys():
            bag[game_id]['console_quantity'][console_id] += quantity
            messages.success(request, f'Successfully added {game.name} on {console.friendly_name} to bag')
        else:
            bag[game_id]['console_quantity'][console_id] = quantity
            messages.success(request, f'Successfully added {game.name} on {console.friendly_name} to bag')
    else:
        bag[game_id] = {'console_quantity': {console_id: quantity}}
        messages.success(request, f'Successfully added {game.name} on {console.friendly_name} to bag')
    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_item(request, game_id):
    try:
        game = get_object_or_404(Game, pk=game_id)
        console_id = request.POST.get('console')
        console = get_object_or_404(Console, pk=console_id)
        bag = request.session.get("bag", {})
        del bag[game_id]['console_quantity'][console_id]
        messages.success(request, f'Successfully removed {game.name} on {console.friendly_name} from bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as err:
        print(err)
        return HttpResponse(status=500)


def adjust_bag(request, game_id):
    if request.POST:
        game = get_object_or_404(Game, pk=game_id)
        console_id = request.POST.get('console')
        console = get_object_or_404(Console, pk=console_id)
        quantity = int(request.POST.get('quantity'))
        bag = request.session.get("bag", {})
        if quantity > 0:
            bag[game_id]['console_quantity'][console_id] = quantity
            messages.success(request, f'Successfully updated quantity of {game.name} on {console.friendly_name}')
        else:
            del bag[game_id]['console_quanity'][console_id]
            messages.success(request, f'Successfully removed {game.name} on {console.friendly_name} from bag')
    request.session['bag'] = bag
    return redirect(reverse('get_bag'))  
