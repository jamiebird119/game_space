from django.shortcuts import render, get_object_or_404, redirect
from games.models import Game
from django.conf import settings
import requests
import json
# Create your views here.


def get_twitch(request, game_id):
    try:
        template = 'twitch/twitch.html'
        game = get_object_or_404(Game, pk=game_id)
        string = 'https://api.twitch.tv/helix/streams?first=10&game_id='
        filter = str(game.twitch_id)
        url = string + filter
        headers = {
            'Client-Id': settings.TWITCH_ID,
            'Authorization': f'Bearer {settings.TWITCH_API_TOKEN}'}
        games = requests.get(url,
                             headers=headers)
        games_info = games.json()
        streams = []
        for item in games_info['data']:
            stream_info = {'username': item['user_name'],
                           'id': item['id'],
                           'thumbnail': item['thumbnail_url'].replace('{width}x{height}', '400x200'),
                           'title': item['title']}
            streams.append(stream_info)
        context = {
            'game': game,
            'streams': streams,
        }
        return render(request, template, context)
    except Exception as err:
        print("Twitch Game Post Failed")
        context = {
            'game': game,
            'error': err
        }
        return render(request, template, context)

def get_stream(request, game_id, username):
    template = 'twitch/twitch_stream.html'
    context = {
        'game_id': game_id,
        'username': username
    }
    return render(request, template, context)