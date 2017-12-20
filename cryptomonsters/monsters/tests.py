from __future__ import unicode_literals
from django.test import TestCase
from .models import Monster


class MonsterModelTestCase(TestCase):
    """Test case for the Monster model."""

    def setUp(self):
        """The initial set up of the tests.

        It makes a User named Bob and gives him a monster.
        """
        self.monster = Monster()

    def test_monster_name_field(self):
        """Test that monster name field has something."""
        assert self.monster.name

    # def test_monster_health_field(self):
    #     """Test that monster health field contains a number between 1 and 10."""
    #     assert self.monster.health in [x for x in range(1, 10)]

    def test_monster_defense_field(self):
        """Test that monster defense field contains a number between 1 and 10."""
        assert self.monster.defense in [x for x in range(1, 10)]

    def test_monster_attack_field(self):
        """Test that monster attack field contains a number between 1 and 10."""
        assert self.monster.attack in [x for x in range(1, 10)]

    def test_monster_type_field(self):
        """Test that monster type field has something."""
        assert self.monster.monster_type
