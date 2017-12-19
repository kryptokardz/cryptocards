"""."""
from monsters.models import Monster
import hashlib
import datetime as date
import json


class Block(object):
    """Create a block that gets appended to our blockchain."""

    def __init__(self, index, timestamp, previous_hash, user, monster_id, proof):
        """Initialize each block."""
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.user = user
        self.monster_id = monster_id
        self.proof = proof
        self.hash = self.block_hash()

    def block_hash(self):
        """Hash all of the attributes for the current block."""
        sha = hashlib.sha256()
        index = str(self.index).encode('utf8')
        timestamp = str(self.timestamp).encode('utf8')
        previous_hash = str(self.previous_hash).encode('utf8')
        user = str(self.user).encode('utf8')
        monster_id = str(self.monster_id).encode('utf8')
        proof = str(self.proof).encode('utf8')
        sha.update(index +
                   timestamp +
                   previous_hash +
                   user +
                   monster_id +
                   proof)
        return sha.hexdigest()

    def view_block(self):
        """."""
        block = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'user': self.user,
            'monster_id': self.monster_id,
            'proof': self.proof,
            'hash': self.hash
        }, sort_keys=True, indent=4,
            separators=(',', ':'))
        return block


class BlockChain(object):
    """Blockchain that contains each block."""

    def __init__(self):
        """Initialize blockchain as list."""
        self.chain = []

        # Create genesis block on init.
        genesis_block = Block(0, date.datetime.now().strftime("%c"), "0", "Genesis", 0, 0000)
        self.chain.append(genesis_block)

    def get_previous_block(self):
        """Get the previous block in the chains."""
        return self.chain[len(self.chain) - 1]

    def new_block(self, user):
        """Add a new block to the chain."""
        # get previous block
        previous_block = self.get_previous_block()
        # run proof of work function
        proof = self.proof_of_work(previous_block)
        index = previous_block.index + 1
        monster_id = previous_block.monster_id + 1
        # TODO: get monster
        timestamp = date.datetime.now().strftime("%c")
        previous_hash = previous_block.hash
        user = user
        new_block = Block(index, timestamp, previous_hash, user, monster_id, proof)
        self.chain.append(new_block)
        return self.chain

    def proof_of_work(self, prev_block):
        """Run proof of work algorithm to mine to block."""
        previous_block = prev_block
        previous_block_index = previous_block.index
        lead_zeros = 4
        nonce = 1
        proof_hash = self.calc_pow_hash(
            previous_block.index, previous_block.timestamp,
            previous_block.previous_hash, previous_block.user,
            previous_block.monster_id, nonce)
        while str(proof_hash[0:lead_zeros]) != '0' * lead_zeros:
            check_previous_block = self.get_previous_block()
            # if another user mines a block first and the block chain
            # changes then start over
            if check_previous_block.index != previous_block_index:
                nonce = 0
                previous_block = check_previous_block
            nonce += 1
            proof_hash = self.calc_pow_hash(
                previous_block.index, previous_block.timestamp,
                previous_block.previous_hash, previous_block.user,
                previous_block.monster_id, nonce)
        return proof_hash

    def calc_pow_hash(self, index, timestamp, previous_hash, user, monster_id, nonce):
        """Calc new hash until the POW requirements are met."""
        sha = hashlib.sha256()
        index = str(index).encode('utf8')
        timestamp = str(timestamp).encode('utf8')
        previous_hash = str(previous_hash).encode('utf8')
        user = str(user).encode('utf8')
        monster_id = str(monster_id).encode('utf8')
        nonce = str(nonce).encode('utf8')
        sha.update(index +
                   timestamp +
                   previous_hash +
                   user +
                   monster_id +
                   nonce)
        return sha.hexdigest()


# blockchain = BlockChain()


def create_monster():
    """."""
    monster = Monster()
    print(monster)

# create_monster()






