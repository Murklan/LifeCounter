from django.conf.urls import url

from . import views

appname = 'game'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game/(?P<game_id>[A-Z0-9]+)/', views.game, name='game'),
]