from __future__ import unicode_literals
from django.test import TestCase
from .models import Monster, random_name, random_id, random_stats, random_type


class MonsterModelTestCase(TestCase):
    """Test case for the Monster model."""

    def setUp(self):
        """The initial set up of the tests.

        It makes a User named Bob and gives him a monster.
        """
        self.monster = Monster()

    def test_monster_name_field(self):
        """Test that monster name field has something."""
        self.assertTrue(self.monster.name)

    def test_monster_health_field(self):
        """Test that monster health field contains a number between 1 and 10."""
        self.assertIn(self.monster.health, [x for x in range(1, 11)])

    def test_monster_defense_field(self):
        """Test that monster defense field contains a number between 1 and 10."""
        self.assertIn(self.monster.defense, [x for x in range(1, 11)])

    def test_monster_attack_field(self):
        """Test that monster attack field contains a number between 1 and 10."""
        self.assertIn(self.monster.attack, [x for x in range(1, 11)])

    def test_monster_type_field(self):
        """Test that monster type field has something."""
        self.assertTrue(self.monster.monster_type)

    def test_random_name_function_works(self):
        """Test that the random name function is returning a string."""
        self.assertIsInstance(random_name(), str)

    def test_random_id_function_works(self):
        """Test that the random id function is returning an int."""
        self.assertIsInstance(random_id(), int)

    def test_random_stats_function_works(self):
        """Test that the random stats function is return an int between 1 and 10."""
        self.assertIsInstance(random_stats(), int)
        self.assertIn(random_stats(), [x for x in range(1, 11)])

    def test_random_type_function_works(self):
        """Test that the random type function is returning a string."""
        self.assertIsInstance(random_type(), str)
