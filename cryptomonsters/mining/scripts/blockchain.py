"""."""
import hashlib
import datetime as date


class Block(object):
    """."""

    def __init__(self, index, timestamp, previous_hash, user, monster_id, this_hash):
        """."""
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.user = user
        self.monster_id = monster_id
        self.hash = this_hash


class BlockChain(object):
    """."""

    def __init__(self):
        """."""
        self.chain = []

        # Create genesis block on init.
        genesis_hash = self.proof_of_work(0, date.datetime.now(), "0", "Genesis", 0)
        genesis_block = Block(0, date.datetime.now(), "0", "Genesis", 0, genesis_hash)
        self.chain.append(genesis_block)

    def calc_hash(self, index, timestamp, previous_hash, user, monster_id, nonce):
        """."""
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

    def get_previous_block(self):
        """."""
        return self.chain[len(self.chain) - 1]

    def new_block(self, user, monster_id):
        """."""
        previous_block = self.get_previous_block()
        index = previous_block.index + 1
        monster_id = previous_block.monster_id + 1
        timestamp = date.datetime.now()
        previous_hash = previous_block.hash
        user = user
        this_hash = self.proof_of_work(index, timestamp, previous_hash, user, monster_id)
        # TODO: Afte Create monster
        # get monster id from DB ????
        new_block = Block(index, timestamp, previous_hash, user, monster_id, this_hash)
        self.chain.append(new_block)
        return self.chain

    def proof_of_work(self, index, timestamp, previous_hash, user, monster_id):
        """."""
        lead_zeros = 4
        nonce = 1
        block_hash = self.calc_hash(
            index, timestamp, previous_hash, user, monster_id, nonce
        )
        while str(block_hash[0:lead_zeros]) != '0' * lead_zeros:
            # import pdb; pdb.set_trace()
            nonce += 1
            block_hash = self.calc_hash(index, timestamp, previous_hash, user, monster_id, nonce)
        return block_hash















