"""."""
from django.conf.urls import url
from mining import views

urlpatterns = [
    url(r'^$', views.miningView, name='mining'),
]