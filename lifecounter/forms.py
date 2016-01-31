from django import forms
from lifecounter.models import Game, Player


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['starting_life', 'max_players']


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', ]
