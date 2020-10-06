from django.shortcuts import render
from .models import Game

# Create your views here.


def games(request):
    games = Game.objects.all()
    template = 'games/games.html'
    content = {
        'games': games
    }
    return render(request, template, content)
