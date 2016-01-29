from rest_framework import serializers, viewsets, filters
from lifecounter.models import Game, Player, CommanderDamage


class CommanderDamageSerializer(serializers.HyperlinkedModelSerializer):
    from_player = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')

    class Meta:
        model = CommanderDamage
        fields = ('from_player', 'cmdr_dmg')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    damage_dealt = CommanderDamageSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('id', 'game', 'name', 'life_total', 'exp_counters', 'poison_counters', 'damage_dealt')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'password', 'max_players', 'starting_life', 'players')


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().prefetch_related('players')
    serializer_class = GameSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('players',)
