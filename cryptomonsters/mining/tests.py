"""."""
from django.test import TestCase
from django.urls import reverse_lazy
from .scripts.blockchain import BlockChain


class MainRoutingTests(TestCase):
    """Tests for the routes in imagersite."""

    def test_mining_route_has_200_response(self):
        """Test that mining route has a 200 response code."""
        response = self.client.get(reverse_lazy('mining'))
        self.assertEqual(response.status_code, 200)

    def test_mining_route_has_content(self):
        """Test that mining route has a contenton the page."""
        response = self.client.get(reverse_lazy('mining'))
        self.assertIn(b'Cryptomonsters', response.content)


class BlockChainTest(TestCase):
    """."""

    def test_genesis_block_is_at_index_zero(self):
        """."""
        blockchain = BlockChain()
        gen = blockchain.chain[0]
        self.assertEqual(gen.user, "Genesis")
        self.assertEqual(gen.index, 0)

    def test_view_block_contains_proper_keys(self):
        """."""
        blockchain = BlockChain()
        gen_info = blockchain.chain[0].view_block()
        self.assertIn('index', gen_info)
        self.assertIn('hash', gen_info)
        self.assertIn('timestamp', gen_info)
        self.assertIn('proof', gen_info)
        self.assertIn('previous_hash', gen_info)
        self.assertIn('user', gen_info)
        self.assertIn('monster_id', gen_info)

    def test_size_one_on_init(self):
        """."""
        blockchain = BlockChain()
        self.assertEqual(len(blockchain.chain), 1)

    def test_add_new_block(self):
        """."""
        blockchain = BlockChain()
        blockchain.new_block('bob')
        self.assertEqual(len(blockchain.chain), 2)

    def test_add_new_blocks_user(self):
        """."""
        blockchain = BlockChain()
        blockchain.new_block('bob')
        self.assertEqual(blockchain.chain[1].user, 'bob')

