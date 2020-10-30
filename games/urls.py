from django.urls import path
from . import views

urlpatterns = [
    path('games', views.games, name="games"),
    path('game_details/<int:game_id>/', views.game_details, name="game_details"),
    path('add_game/', views.add_game, name="add_game"),
]
