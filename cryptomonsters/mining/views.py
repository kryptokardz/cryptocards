"""Base views for cryptomonsters."""
from django.shortcuts import render
from mining.scripts import blockchain


def miningView(request):
    """."""
    # request.user.username = 'bob'
    new_blockchain = blockchain.blockchain.new_block('bob')
    # import pdb; pdb.set_trace()
    return render(request, 'mining/mining.html')


# TODO: create mining "home" page
# TODO: page to show monster after monster is mined
# TODO: finish view route that does the mining