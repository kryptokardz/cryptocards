"""Monsters url."""
from django.conf.urls import url

from monsters import views


urlpatterns = [
    url(r'^$', views.MonstersView.as_view(), name='all_monsters'),
]
