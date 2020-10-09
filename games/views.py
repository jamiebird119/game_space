from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Game
from django.db.models import Q

# Create your views here.


def games(request):
    query = None
    games = Game.objects.all()
    template = 'games/games.html'
    
    # Below Code taken from CI E-Commerce project
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error('You have not entered a search criteria!')
                return redirect(reverse('games'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(consoles__name__icontains=query) | Q(genres__name__icontains=query)
            games = games.filter(queries).distinct()

    context = {
        'games': games,
        'search_term': query
    }

    return render(request, template, context)


def game_details(request, game_id):
    template = 'games/game_details.html'
    game = get_object_or_404(Game, pk=game_id)
    context = {
        'game': game
    }
    return render(request, template, context)
