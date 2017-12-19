"""Base views for cryptomonsters."""
from django.shortcuts import render
from monsters.models import Monster
from mining.scripts import blockchain
from django.views.generic import ListView, DetailView
import json


class MiningHomeView(ListView):
    """."""

    model = Monster
    template_name = 'mining/mining.html'


class MiningNewBlock(ListView):
    """."""

    model = Monster
    template_name = 'mining/new_block.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(MiningNewBlock, self).get_context_data(**kwargs)
        user = context['view'].request.user
        # monster = json.loads(blockchain.blockchain.new_block(user))
        monster = blockchain.blockchain.new_block(user)
        context['data'] = monster
        # import pdb; pdb.set_trace()
        return context


