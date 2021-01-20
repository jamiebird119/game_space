from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.contrib import messages

from .models import Game
from .forms import GameForm


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
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(
                consoles__friendly_name__icontains=query) | Q(genres__name__icontains=query)
            games = games.filter(queries).distinct()
            if query == "":
                messages.warning(request, 'You have not entered a search criteria!')
                return redirect(reverse('games'))

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


@login_required
def add_game(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. Only store owners can add products')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()
            messages.success(request, 'Game successfully added!')
            return redirect(reverse('game_details', args=[game.id]))
        else:
            messages.error(
                request,  f'Failed to add product. Please ensure form is valid : {form.errors}')
    template = "games/add_game.html"
    form = GameForm()
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_game(request, game_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. Only store owners can add games')
        return redirect(reverse('home'))
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Game {game.name} successfully edited')
            return redirect(reverse('game_details', args=[game_id]))
        else:
            messages.error(
                request,  'Failed to add game. Please ensure form is valid')
    form = GameForm(instance=game)
    template = "games/edit_game.html"
    context = {
        'game': game,
        'form': form,
    }
    return render(request, template, context)


@login_required
def remove_game(request, game_id):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry. Only store owners can add games')
        return redirect(reverse('home'))

    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    messages.success(request, 'Game successfully deleted')
    return redirect(reverse('games'))


@login_required
def product_management(request):
    template = 'games/product_management.html'
    context = {
        'games': Game.objects.all(),
    }
    return render(request, template, context)
