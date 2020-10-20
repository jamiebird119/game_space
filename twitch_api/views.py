from django.shortcuts import render, get_object_or_404
from games.models import Game
from django.conf import settings
import requests

TWITCH_STREAM_URI = 'https://api.twitch.tv/helix/streams?first=12&game_id='
TWITCH_AUTH_URI = 'https://id.twitch.tv/oauth2/token'
TWITCH_TEMPLATE = 'twitch/twitch.html'


def get_stream_info(request, game):
    try:
        url = TWITCH_STREAM_URI + str(game.twitch_id)
        headers = {
            'Client-Id': settings.TWITCH_ID,
            'Authorization': f'Bearer {settings.TWITCH_API_TOKEN}'}
        games = requests.get(url,
                             headers=headers)
        games_info = games.json()
        print(games_info)
        streams = []
        for item in games_info['data']:
            stream_info = {'username': item['user_name'],
                           'id': item['id'],
                           'thumbnail': item['thumbnail_url'].replace('{width}x{height}', '350x200'),
                           'title': item['title'],
                           'viewers': item['viewer_count']}
            streams.append(stream_info)
        context = {
            'game': game,
            'streams': streams,
        }
        return render(request, TWITCH_TEMPLATE, context)
    except Exception as err:
        print("Twitch Game Post Failed")
        context = {
            'game': game,
            'error': err
        }
        return render(request, TWITCH_TEMPLATE, context)


def auth_and_get_stream_info(request, game):
    try:
        params = (
            ('client_id', settings.TWITCH_ID),
            ('client_secret', settings.TWITCH_SECRET),
            ('grant_type', 'client_credentials'),
        )
        response = requests.post(TWITCH_AUTH_URI, data=params)
        if response:
            if response.status_code == 200:
                access_token = response.json().get('access_token')
                request.session['auth_token'] = access_token
                return get_stream_info(request, game)
            else:
                # TODO Error response
                ...
        else:
            print("Twitch Auth Failed")
            context = {
                'game': game,
                'error': 'An error has occurred. Please try again later or contact customer support.'
            }
            return render(request, TWITCH_TEMPLATE, context)
    except Exception as err:
        print("Twitch Auth Failed")
        context = {
            'game': game,
            'error': err
        }
        return render(request, TWITCH_TEMPLATE, context)


def get_twitch(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    if 'auth_token' in request.session:
        return get_stream_info(request, game)
    else:
        return auth_and_get_stream_info(request, game)


def get_stream(request, game_id, username):
    template = 'twitch/twitch_stream.html'
    game = get_object_or_404(Game, pk=game_id)
    context = {
        'game': game,
        'username': username
    }
    return render(request, template, context)
