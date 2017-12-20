"""Base views for cryptomonsters."""
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView

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
        # monster = json.loads(blockchain.blockchain.new_block(user))
        monster = blockchain.new_block(user)
        context['data'] = monster
        # import pdb; pdb.set_trace()
        return context
