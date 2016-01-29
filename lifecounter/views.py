from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Game


def index(request):
    return HttpResponse("Hello, world")


def game(request, game_id):
    gameset = get_object_or_404(Game, pk=game_id)
    return render(request, 'lifecounter/game.html', {'game': gameset})

