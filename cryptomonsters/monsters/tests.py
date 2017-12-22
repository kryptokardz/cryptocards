"""Test monster app."""
from __future__ import unicode_literals

from django.test import TestCase

from monsters.scripts import stories

from monsters.models import Monster, random_name, random_stats, random_type


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
        """Test monster health field contains a number between 1 and 10."""
        self.assertIn(self.monster.health, [x for x in range(1, 20)])

    def test_monster_defense_field(self):
        """Test monster defense field contains a number between 1 and 10."""
        self.assertIn(self.monster.defense, [x for x in range(1, 20)])

    def test_monster_attack_field(self):
        """Test monster attack field contains a number between 1 and 10."""
        self.assertIn(self.monster.attack, [x for x in range(1, 20)])

    def test_monster_type_field(self):
        """Test that monster type field has something."""
        self.assertTrue(self.monster.monster_type)

    def test_random_name_function_works(self):
        """Test that the random name function is returning a string."""
        self.assertIsInstance(random_name(), str)

    def test_random_stats_function_works(self):
        """Test andom stats function is return an int between 1 and 10."""
        self.assertIsInstance(random_stats(), int)
        self.assertIn(random_stats(), [x for x in range(1, 20)])

    def test_random_type_function_works(self):
        """Test that the random type function is returning a string."""
        self.assertIsInstance(random_type(), str)

    def test_wizard_story(self):
        """Test wizard story."""
        s = stories.wizard_story('eddietheblob')
        self.assertIn(u'first 1000 years of life', s)

    def test_bear_story(self):
        """Test bear story."""
        s = stories.bear_story('eddietheblob')
        self.assertIn(u'made a career of burglarizing unsuspecting', s)

    def test_barbarian_story(self):
        """Test barbarian story."""
        s = stories.barbarian_story('eddietheblob')
        self.assertIn(u'Pillaging is their game', s)

    def test_goblin_story(self):
        """Test goblin story."""
        s = stories.goblin_story('eddietheblob')
        self.assertIn(u'servant of the great demon Shushushasha', s)

    def test_skeleton_story(self):
        """Test skeleton story."""
        s = stories.skeleton_story('eddietheblob')
        self.assertIn(u'favorite movie is The Wizard of Oz', s)

    def test_zombie_story(self):
        """Test zombie story."""
        s = stories.zombie_story('eddietheblob')
        self.assertIn(u'only one way to eat a steak', s)

    def test_slime_story(self):
        """Test slime story."""
        s = stories.slime_story('eddietheblob')
        self.assertIn(u'slimey, two dimensional ball of hate', s)

    def test_wolf_story(self):
        """Test wolf story."""
        s = stories.wolf_story()
        self.assertTrue(u'woof' == s)

    def test_minotaur_story(self):
        """Test minotaur story."""
        s = stories.minotaur_story('eddietheblob')
        self.assertIn(u'probably just angry because they are as lost', s)
