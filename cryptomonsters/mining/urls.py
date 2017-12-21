"""Mining views."""
from django.conf.urls import url

from mining import views

urlpatterns = [
    url(r'^$', views.MiningHomeView.as_view(), name='mining_home'),
    url(r'^create/$', views.MiningNewBlock.as_view(),
        name='mining_new_block'),
    url(r'^blockchain/$', views.blockchain_view, name='blockchain'),
]
