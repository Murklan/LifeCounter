from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'', include('lifecounter.urls')),
    url(r'^api/', include('lifecounter.api_urls')),
    url(r'^admin/', admin.site.urls),
]
