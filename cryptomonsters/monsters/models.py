"""Moster model."""
from django.contrib.auth.models import User
from django.db import models
from faker import Faker
from random import randint, choice

fake = Faker()


def random_name():
    return fake.first_name()


def random_stats():
    return randint(1, 10)


def random_id():
    return hash(''.join(fake.words()))


class Monster(models.Model):
    """Create new monster model."""
    TYPES = (
        ('Slime'),
        ('Skeleton'),
        ('Zombie'),
        ('Minotaur')
    )

    user = models.ForeignKey(
        User,
        related_name='monsters',
        on_delete=models.CASCADE)
    img_file = models.ImageField(upload_to='monsters_dir')
    name = models.CharField(max_length=30, default=random_name)
    health = models.IntegerField(default=random_stats)
    defense = models.IntegerField(default=random_stats)
    attack = models.IntegerField(default=random_stats)
    monster_type = models.CharField(max_length=100, default=choice(TYPES))
    unique_id = models.BigIntegerField(default=random_id)

    def __str__(self):
        """Render as string."""
        return self.title
