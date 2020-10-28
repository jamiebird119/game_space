from django.shortcuts import render, get_object_or_404
from games.models import Game
from django.conf import settings
import requests

TWITCH_STREAM_URI = 'https://api.twitch.tv/helix/streams?first=12&game_id='
TWITCH_AUTH_URI = 'https://id.twitch.tv/oauth2/token'
TWITCH_TEMPLATE = 'twitch/twitch.html'


def get_stream_info(request, game, auth):
    try:
        url = TWITCH_STREAM_URI + str(game.twitch_id)
        request.session['auth_token'] = auth
        headers = {
            'Client-Id': settings.TWITCH_ID,
            'Authorization': f"Bearer {auth}"}
        games = requests.get(url,
                             headers=headers)
        games_info = games.json()
        if len(games_info["data"]) == 0:
            error = "There are currently no streams available for this game. Please try again later."
            context = {
                'game': game,
                'error': error
            }
            return render(request, TWITCH_TEMPLATE, context)
        else:
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
        print(err)
        error = "There are currently no streams available for this game. Please try again later."
        context = {
            'game': game,
            'error': error
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
                auth = access_token
                print(access_token)
                return get_stream_info(request, game, auth=auth)
            else:
                context = {
                    'game': game,
                    'error': 'An error has occurred. Please try again later or contact customer support.'
                }
                return render(request, TWITCH_TEMPLATE, context)
        else:
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
        return get_stream_info(request, game, auth=request.session['auth_token'])
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
