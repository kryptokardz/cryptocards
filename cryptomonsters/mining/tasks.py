from __future__ import absolute_import, unicode_literals
from celery import shared_task
from mining import scripts
import time


@shared_task(name='tasks.p_o_w')
def p_o_w(previous_block, ser_user):
    """Async function that then calls the proof of work mining function."""
    bc = scripts.blockchain.BlockChain()
    data = bc._proof_of_work(previous_block, ser_user)
    return 'monster {} is created, nonce: {}'.format(data[1], data[0])
