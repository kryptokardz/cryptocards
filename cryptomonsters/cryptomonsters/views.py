"""Base views for cryptomonsters."""
from django.shortcuts import render


def home_view(request):
    """Cryptomonster home view."""
    return render(request, 'cryptomonsters/home.html')
