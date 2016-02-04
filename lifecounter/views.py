from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from .models import Game, Player
from .forms import GameForm, PlayerForm

import passwordgenerator

pw = passwordgenerator


def index(request):
    return render(request, 'lifecounter/index.html')


def show_game(request, game_id):
    gameset = get_object_or_404(Game, pk=game_id)
    return render(request, 'lifecounter/game.html', {'game': gameset})


def create_game(request):
    form = {'form': GameForm}
    return render(request, 'lifecounter/new_game.html', form)


def start_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.password = pw.generate_password()
            new_game.save()
            return HttpResponseRedirect('/game/' + str(new_game.id))
        else:
            form = GameForm()
        return render(request, 'lifecounter/game.html', {'form': form})


def register_player(request):
    form = {'form': PlayerForm}
    return render(request, 'lifecounter/player.html', form)


def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            joined_game = Game.objects.get(password=form.cleaned_data['pw'])
            if joined_game.players.count() < joined_game.max_players:
                new_player = Player(name=form.cleaned_data['name'],
                                    game=joined_game,
                                    life_total=joined_game.starting_life)
                new_player.save()
                return HttpResponseRedirect('/game/' + str(new_player.game.id))
            else:
                return HttpResponse('That lobby is full. Try joining another one!')
        else:
            form = PlayerForm()
        return render(request, 'lifecounter/player.html', {'form': form})



