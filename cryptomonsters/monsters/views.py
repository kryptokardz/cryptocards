"""Monster views."""
from django.views.generic import ListView

from monsters.models import Monster

from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


class MonstersView(ListView):
    """View all monsters."""

    model = Monster
    template_name = 'monsters/all_monsters.html'
    context_object_name = 'monsters'
    paginate_by = 24

    def get_queryset(self):
        """Request users profile."""
        import pdb; pdb.set_trace()
        return Monster.objects.all()
