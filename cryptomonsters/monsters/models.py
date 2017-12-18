"""Moster model."""
from django.contrib.auth.models import User

from django.db import models


class Monster(models.Model):
    """Create new monster model."""

    user = models.ForeignKey(
        User,
        related_name='monsters',
        on_delete=models.CASCADE)
    img_file = models.ImageField(upload_to='monsters_dir')
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField()

    def __str__(self):
        """Render as string."""
        return self.title
