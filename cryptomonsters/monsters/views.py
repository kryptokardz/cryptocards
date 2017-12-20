"""Monster views."""
from django.views.generic import ListView

from monsters.models import Monster


class MonstersView(ListView):
    """View all monsters."""

    model = Monster
    template_name = 'monsters/all_monsters.html'
    context_object_name = 'monsters'

    def get_queryset(self):
        """Request users profile."""
        return Monster.objects.all()
