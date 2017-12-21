"""Base views for cryptomonsters."""
from monsters.models import Monster
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView


def home_view(request):
    """Cryptomonster home view."""
    return render(request, 'cryptomonsters/home.html')


class ProfileView(LoginRequiredMixin, DetailView):
    """Display user data."""
    redirect_field_name = '/accounts/login'
    template_name = 'cryptomonsters/profile.html'
    context_object_name = 'user'
    redirect_field_name = '/accounts/login'

    def get_object(self):
        """Return user data."""
        return self.request.user


class UpdateUser(LoginRequiredMixin, UpdateView):
    """Update user information."""

    model = User
    fields = [
        'first_name',
        'last_name',
        'email',
    ]
    template_name = 'cryptomonsters/user_update_form.html'
    context_object_name = 'user'
    redirect_field_name = '/accounts/login'

    def get_object(self):
        """Fill form data."""
        return self.request.user
