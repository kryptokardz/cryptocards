from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Monster
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Create a test User."""

    class Meta:
        model = User

    username = 'bob'
    email = 'bob@bob.com'


class MonsterModelTestCase(TestCase):
    """Test case for the Monster model."""

    def setUp(self):
        """The initial set up of the tests.

        It makes a User named Bob and gives him a monster.
        """
        self.user = UserFactory.create()
        self.user.set_password('password')
        self.user.save()

        self.monster = Monster()
        self.monster.save()

        self.user.monsters.add(self.monster)

    def tearDown(self):
        """Goes in and deletes our Bob user."""
        User.objects.get(username='bob').delete()

    def test_monster_associates_with_user(self):
        self.assertEqual(self.user.monsters.count(), 1)
