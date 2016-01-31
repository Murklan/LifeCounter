from django import forms
from lifecounter.models import Game, Player


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['starting_life', 'max_players']


class PlayerForm(forms.Form):

    name = forms.CharField(label='Nickname', max_length=20)
    pw = forms.CharField(label='Password', max_length=5)
