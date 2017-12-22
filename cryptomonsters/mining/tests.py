"""Tests for mining."""
import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy

import factory

from mining.scripts.blockchain import BlockChain


class BlockChainTest(TestCase):
    """Class to test blockchain."""

    # def test_genesis_block_is_at_index_zero(self):
    #     """Test genesis block in blockchain."""
    #     blockchain = BlockChain()
    #     gen = blockchain.chain[0]
    #     self.assertEqual(gen.user, "Genesis")
    #     self.assertEqual(gen.index, 0)

    def test_view_block_contains_proper_keys(self):
        """Test block contains proper keys."""
        blockchain = BlockChain()
        gen_info = blockchain.chain[0]
        self.assertIn('index', gen_info)
        self.assertIn('hash', gen_info)
        self.assertIn('timestamp', gen_info)
        self.assertIn('proof', gen_info)
        self.assertIn('previous_hash', gen_info)
        self.assertIn('user', gen_info)

    def test_size_one_on_init(self):
        """Test size when init one chain."""
        blockchain = BlockChain()
        with open('cryptomonsters/static/blockchain/blockchain.json') as file:
            chain = json.load(file)
        self.assertEqual(len(blockchain.chain), len(chain))


class BlockChainViewTest(TestCase):
    """Test the blockchain view."""

    def test_blockchain_view_template(self):
        """Test that the blockchain view uses proper html."""
        response = self.client.get(reverse_lazy('blockchain'))
        self.assertTemplateUsed(response, 'mining/blockchain.html')

    def test_blockchain_returns_200_ok(self):
        """Test that blockchain returns 200 ok."""
        response = self.client.get(reverse_lazy('blockchain'))
        self.assertEqual(response.status_code, 200)

    def test_blockchain_view_shows_health(self):
        """Test that the blockchain view shows genesis block."""
        response = self.client.get(reverse_lazy('blockchain'))
        self.assertIn(b'Health', response.content)

    def test_blockchain_view_renders_hash(self):
        """Test that the blockchain view renders hash."""
        response = self.client.get(reverse_lazy('blockchain'))
        self.assertIn(b'Hash:', response.content)

    def test_blockchain_view_includes_monsters(self):
        """Test blockchain view includes monsters."""
        response = self.client.get(reverse_lazy('blockchain'))
        self.assertIn(b'Monster Name', response.content)


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for fake User."""

    class Meta:
        """Meta."""

        model = User

    username = factory.Sequence(lambda n:
                                '{}{}'.format(factory.Faker('first_name'), n))
    email = factory.Faker('email')


class MiningViews(TestCase):
    """Test mininig views."""

    def setUp(self):
        """Set up a user for testing login.."""
        user = UserFactory(username='bob', email='bob@bob.net')
        user.set_password('password')
        user.save()

    def test_start_mining_on_page(self):
        """Test start mining on start page."""
        self.client.post(reverse_lazy('login'), {
            'username': 'bob',
            'password': 'password'
        }, follow=True)
        response = self.client.get(reverse_lazy('mining_home'))
        self.assertIn(b'Time to mine!', response.content)
