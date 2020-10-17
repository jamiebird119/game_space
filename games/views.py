from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Game
from django.conf import settings
import requests
import json

# Create your views here.


def games(request):
    query = None
    games = Game.objects.all()
    template = 'games/games.html'
    sort = None
    direction = None
    # Below Code taken from CI E-Commerce project / editted
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                games = games.annotate(lower_name=Lower('name'))
            if sortkey == 'genre':
                sortkey = 'genre__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            games = games.order_by(sortkey)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error('You have not entered a search criteria!')
                return redirect(reverse('games'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(
                consoles__friendly_name__icontains=query) | Q(genres__name__icontains=query)
            games = games.filter(queries).distinct()

    current_sorting = f'{sort}_{direction}'
    context = {
        'games': games,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


def game_details(request, game_id):
    template = 'games/game_details.html'
    game = get_object_or_404(Game, pk=game_id)
    context = {
        'game': game
    }
    return render(request, template, context)


