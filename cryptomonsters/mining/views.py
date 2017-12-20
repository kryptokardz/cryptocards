"""Base views for cryptomonsters."""
from django.shortcuts import render
from monsters.models import Monster
from mining.scripts.blockchain import BlockChain
from django.views.generic import ListView, DetailView

blockchain = BlockChain()


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
        monster = blockchain.new_block(user)
        context['data'] = monster
        return context

