"""Base views for cryptomonsters."""
from django.shortcuts import render
from mining.scripts import blockchain


def miningView(request):
    """."""
    # request.user.username = 'bob'
    # new_blockchain = blockchain.blockchain.new_block(request.user.username)
    # import pdb; pdb.set_trace()
    return render(request, 'cryptomonsters/mining.html')