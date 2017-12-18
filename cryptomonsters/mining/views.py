"""Base views for cryptomonsters."""
from django.shortcuts import render
from mining.scripts import blockchain



def miningView(request):
    """Cryptomonster home view."""
    # request.user.username = 'bob'
    # new_blockchain = blockchain.blockchain.new_block(request.user.username)
    return render(request, 'cryptomonsters/mining.html')