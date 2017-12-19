"""."""
from django.conf.urls import url
from mining import views

urlpatterns = [
    url(r'^$', views.MiningHomeView.as_view(), name='mining_home'),
    url(r'^create/$', views.MiningNewBlock.as_view(), name='mining_new_block')
]