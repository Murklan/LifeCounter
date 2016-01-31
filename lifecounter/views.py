from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Game, Player
from .forms import GameForm, PlayerForm
from .serializers import PlayerSerializer
import passwordgenerator

pw = passwordgenerator


def index(request):
    form = {'form': GameForm}
    return render(request, 'lifecounter/index.html', form)


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


@api_view(['PUT', 'GET'])
def change_life_total(request, player_id):
    if request.method == 'GET':
        player = Player.objects.all()
        serializer = PlayerSerializer(player, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == 'PUT':
        player = Player.objects.get(id=player_id)
        data = {'id': player.id,
                'life_total': player.life_total + 1,
                'name': player.name,
                'game': 'http://localhost:8000/api/game/'+str(player.game.id)+'/'}
        serializer = PlayerSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

