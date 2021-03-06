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
    """View to start mining."""

    model = Monster
    template_name = 'mining/mining.html'
    redirect_field_name = '/accounts/login'


class MiningStart(LoginRequiredMixin, ListView):  # pragma: no cover
    """View to show goblin gif while mining is happening."""

    model = Monster
    template_name = 'mining/mining_start.html'
    redirect_field_name = '/accounts/login'

    def get_context_data(self, **kwargs):
        """Return the context id which is key for redis."""
        context = super(MiningStart, self).get_context_data(**kwargs)
        user = context['view'].request.user
        async_id = blockchain.new_block(user)
        context['async_id'] = async_id
        context['ready'] = False
        return context


class MiningNewBlock(LoginRequiredMixin, ListView):  # pragma: no cover
    """Check if monster is done being mined for."""

    model = Monster
    template_name = 'mining/mining_start.html'
    redirect_field_name = '/accounts/login'

    def get_context_data(self, **kwargs):
        """If the monster is ready then send it to view else keep waiting."""
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
    with open('cryptomonsters/static/blockchain/blockchain.json') as file:
        chain = json.load(file)
    page = request.GET.get('page', 1)
    paginator = Paginator(chain[::-1], 5)
    try:
        blocks = paginator.page(page)
    except PageNotAnInteger:  # pragma: no cover
        blocks = paginator.page(1)
    except EmptyPage:  # pragma: no cover
        blocks = paginator.page(paginator.num_pages)

    return render(request, 'mining/blockchain.html', {'blockchain': blocks})
