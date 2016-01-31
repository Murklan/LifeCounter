from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Game
from .forms import GameForm, PlayerForm
import passwordgenerator

pw = passwordgenerator


def index(request):
    forms = {'form': GameForm}
    return render(request, 'lifecounter/index.html', forms)


def game(request, game_id):
    gameset = get_object_or_404(Game, pk=game_id)
    return render(request, 'lifecounter/game.html', {'game': gameset})


def create_game(request):
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
