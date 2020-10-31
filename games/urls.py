from django.urls import path
from . import views

urlpatterns = [
    path('games', views.games, name="games"),
    path('game_details/<int:game_id>/', views.game_details, name="game_details"),
    path('add_game/', views.add_game, name="add_game"),
    path('edit_game/<int:game_id>/', views.edit_game, name="edit_game"),
    path('remove_game/<int:game_id>/', views.remove_game, name="remove_game"),
    path('product_management/', views.product_management, name="product_management"),
]
