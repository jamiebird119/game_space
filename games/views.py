from django.shortcuts import render, get_object_or_404
from .models import Game
from django.db.models import Q

# Create your views here.


def games(request):
    query = None
    games = Game.objects.all()
    template = 'games/games.html'
    content = {
        'games': games
    }
    return render(request, template, content)


def game_details(request, game_id):
    template = 'games/game_details.html'
    game = get_object_or_404(Game, pk=game_id)
    content = {
        'game': game
    }
    return render(request, template, content)
