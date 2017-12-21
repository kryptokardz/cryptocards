"""Base views for cryptomonsters."""
import json

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from mining.scripts.blockchain import BlockChain

from monsters.models import Monster


blockchain = BlockChain()


class MiningHomeView(LoginRequiredMixin, ListView):
    """."""

    model = Monster
    template_name = 'mining/mining.html'
    redirect_field_name = '/accounts/login'


class MiningNewBlock(LoginRequiredMixin, ListView):
    """."""

    model = Monster
    template_name = 'mining/new_block.html'
    context_object_name = 'data'
    redirect_field_name = '/accounts/login'

    def get_context_data(self, **kwargs):
        """."""
        context = super(MiningNewBlock, self).get_context_data(**kwargs)
        user = context['view'].request.user
        monster = blockchain.new_block(user)
        context['data'] = monster
        return context


def blockchain_view(request):
    """Veiw the blockchain."""
    if settings.DEBUG:
        with open('cryptomonsters/static/blockchain/blockchain.json') as file:
            chain = json.load(file)
    else:
        with open(settings.STATIC_URL + 'blockchain/blockchain.json') as file:
            chain = json.load(file)
    return render(request, 'mining/blockchain.html', {'blockchain': chain})
