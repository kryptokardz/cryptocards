from __future__ import absolute_import, unicode_literals
from celery import shared_task
from mining.scripts import blockchain
import time


@shared_task(name='tasks.rev')
def rev(string):
    time.sleep(10)
    a = string[::-1]
    return a


@shared_task
def p_o_w(previous_block, ser_user):
    """."""
    blckchain = blockchain.BlockChain()
    i = 0
    top = 99999999
    while i < top:
        i += 1
    blckchain._proof_of_work(previous_block, ser_user)
    return 'monster is created'

