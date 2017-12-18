from cryptomonsters.views import home_view

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', home_view, name='home'),
]