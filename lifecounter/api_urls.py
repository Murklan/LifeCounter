from django.conf.urls import url, include
from lifecounter.serializers import GameViewSet, PlayerViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'game', GameViewSet)
router.register(r'player', PlayerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]