from django.urls import path
from . import views


urlpatterns = [
    path('twitch/<game_id>/', views.get_twitch, name="get_twitch"),
    path('get_stream/<game_id>/<username>', views.get_stream, name="get_stream"),
]