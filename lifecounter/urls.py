from django.conf.urls import url, include

from . import views

appname = 'lifecounter'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game/(?P<game_id>[0-9]+)/', views.show_game, name='game'),
    url(r'^create_game/', views.create_game, name='create_game'),
    url(r'^start_game/', views.start_game, name='start_game'),
    url(r'^register_player/', views.register_player, name='register_player'),
    url(r'^create_player/', views.create_player, name='create_player'),
]