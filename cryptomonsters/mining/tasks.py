from __future__ import absolute_import, unicode_literals
from celery import shared_task
from mining.scripts import blockchain
import time


@shared_task(name='tasks.p_o_w')
def p_o_w(previous_block, ser_user):
    """."""
    bc = blockchain.BlockChain()
    bc._proof_of_work(previous_block, ser_user)
    return 'monster is created'

