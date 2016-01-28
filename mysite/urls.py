"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from lifecounter.models import Game, Player, CommanderDamage
from rest_framework import routers, serializers, viewsets


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


router = routers.DefaultRouter()
router.register(r'games', GameViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
