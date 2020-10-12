from django.urls import path
from . import views

urlpatterns = [
    path('games', views.games, name="games"),
    path('game_details/<game_id>', views.game_details, name="game_details"),
    path('game_twitch/<game_id>', views.game_twitch, name="game_twitch"),
]
