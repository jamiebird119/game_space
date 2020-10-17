from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from games.models import Game
# Create your views here.


def get_bag(request):
    template = 'bag/bag.html'
    context = {

    }
    return render(request, template, context)


def add_to_bag(request, game_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    console = request.POST.get('console')
    bag = request.session.get('bag', {})
    if game_id in list(bag.keys()):
        if console in bag[game_id]['console_quantity'].keys():
            bag[game_id]['console_quantity'][console] += quantity
            print(bag)
        else:
            bag[game_id]['console_quantity'][console] = quantity
            print(bag)
    else:
        bag[game_id] = {'console_quantity': {console: quantity}}
        print(bag)
    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_item(request, game_id):
    try:
        console = request.POST.get('console')
        bag = request.session.get("bag", {})
        del bag[game_id]['console_quantity'][console]
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as err:
        print(err)
        return HttpResponse(status=500)


def adjust_bag(request, game_id):
    if request.POST:
        console = request.POST.get('console')
        quantity = int(request.POST.get('quantity'))
        bag = request.session.get("bag", {})
        if quantity > 0:
            bag[game_id]['console_quantity'][console] = quantity
        else:
            del bag[game_id]['console_quanity'][console]
    request.session['bag'] = bag
    return redirect(reverse('get_bag'))  
