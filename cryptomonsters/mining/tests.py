"""."""
from django.test import TestCase
from .scripts.blockchain import BlockChain
import json


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
        with open('cryptomonsters/static/blockchain/blockchain.json') as file:
            chain = json.load(file)
        self.assertEqual(len(blockchain.chain), len(chain))

    def test_add_new_block(self):
        """."""
        blockchain = BlockChain()
        with open('cryptomonsters/static/blockchain/blockchain.json') as file:
            chain = json.load(file)
        blockchain.new_block('bob')
        self.assertEqual(len(blockchain.chain), len(chain))

    def test_add_new_blocks_user(self):
        """."""
        blockchain = BlockChain()
        blockchain.new_block('bob')
        self.assertEqual(blockchain.chain[1].User, 'bob')

