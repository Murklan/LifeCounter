from django.conf.urls import url, include
from lifecounter.serializers import GameViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'game', GameViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]