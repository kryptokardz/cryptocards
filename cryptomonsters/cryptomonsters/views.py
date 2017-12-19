"""Base views for cryptomonsters."""
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView

from monsters.models import Monster


def home_view(request):
    """Cryptomonster home view."""
    return render(request, 'cryptomonsters/home.html')


class ProfileView(DetailView):
    """Display user data."""

    redirect_field_name = '/accounts/login'
    template_name = 'cryptomonsters/profile.html'
    context_object_name = 'user'

    def get_object(self):
        """Return user data."""
        return self.request.user
