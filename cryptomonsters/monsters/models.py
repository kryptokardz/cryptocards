"""Moster model."""
from django.contrib.auth.models import User
from django.db import models
from faker import Faker
from random import randint, choice

fake = Faker()


def _random_name():
    """Return a random first name using Faker."""
    return fake.first_name()


def _random_stats():
    """Return a random integer between 1 and 10 using Faker."""
    return randint(1, 10)


def _random_type():
    """Return type of monster."""
    types = (
        ('Slime'),
        ('Skeleton'),
        ('Zombie'),
        ('Blue Wizard'),
        ('Red Wizard'),
        ('Bear'),
        ('Wolf'),
        ('Barbarian'),
        ('Minotaur'),
        ('Goblin'),
    )
    return choice(types)


class Monster(models.Model):
    """Create new monster model."""

    user = models.ForeignKey(
        User,
        related_name='monsters',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default=_random_name)
    health = models.IntegerField(default=_random_stats)
    defense = models.IntegerField(default=_random_stats)
    attack = models.IntegerField(default=_random_stats)
    monster_type = models.CharField(max_length=100, default=_random_type)
    unique_id = models.IntegerField(default=0)
    img_file = models.ImageField()

    def __str__(self):
        """Render as string."""
        return '{} the {}'.format(self.name, self.monster_type)
