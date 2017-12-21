"""Base views for cryptomonsters."""
import json

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView
from mining.scripts.blockchain import BlockChain
from monsters.models import Monster
from django.urls import reverse_lazy
import redis
import json

blockchain = BlockChain()
conn = redis.Redis('localhost')


class MiningHomeView(LoginRequiredMixin, ListView):
    """."""

    model = Monster
    template_name = 'mining/mining.html'
    redirect_field_name = '/accounts/login'


class MiningStart(LoginRequiredMixin, ListView):
    """."""

    model = Monster
    template_name = 'mining/mining_start.html'
    redirect_field_name = '/accounts/login'

    def get_context_data(self, **kwargs):
        """."""
        context = super(MiningStart, self).get_context_data(**kwargs)
        user = context['view'].request.user
        async_id = blockchain.new_block(user)
        context['async_id'] = async_id
        context['ready'] = False
        return context


class MiningNewBlock(LoginRequiredMixin, ListView):
    """."""

    model = Monster
    template_name = 'mining/mining_start.html'
    redirect_field_name = '/accounts/login'

    def get_context_data(self, **kwargs):
        """."""
        context = super(MiningNewBlock, self).get_context_data(**kwargs)
        async_id = self.request.GET['id']
        try:
            json.loads(conn.get("celery-task-meta-{}".format(async_id)).decode('utf8'))
            context['ready'] = True
            user = context['view'].request.user
            monster = user.monsters.last()
            context['data'] = monster
            return context
        except AttributeError:
            context['async_id'] = async_id
            context['wait'] = True
            return context


def blockchain_view(request):
    """View the blockchain."""
    if settings.DEBUG:
        with open('cryptomonsters/static/blockchain/blockchain.json') as file:
            chain = json.load(file)
    else:
        with open(settings.STATIC_URL + 'blockchain/blockchain.json') as file:
            chain = json.load(file)
    page = request.GET.get('page', 1)
    paginator = Paginator(chain[::-1], 5)
    try:
        blocks = paginator.page(page)
    except PageNotAnInteger:
        blocks = paginator.page(1)
    except EmptyPage:
        blocks = paginator.page(paginator.num_pages)

    return render(request, 'mining/blockchain.html', {'blockchain': blocks})

