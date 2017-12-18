"""."""
import hashlib
import datetime as date


class Block(object):
    """."""

    def __init__(self, index, timestamp, previous_hash, user, monster_id, proof):
        """."""
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.user = user
        self.monster_id = monster_id
        self.proof = proof
        self.hash = self.block_hash()

    def block_hash(self):
        """."""
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


class BlockChain(object):
    """."""

    def __init__(self):
        """."""
        self.chain = []

        # Create genesis block on init.
        genesis_block = Block(0, date.datetime.now(), "0", "Genesis", 0, 0000)
        self.chain.append(genesis_block)

    def get_previous_block(self):
        """."""
        return self.chain[len(self.chain) - 1]

    def new_block(self, user):
        """."""
        previous_block = self.get_previous_block()
        # run proof of work function
        proof = self.proof_of_work(previous_block)
        index = previous_block.index + 1
        monster_id = previous_block.monster_id + 1
        # TODO: get monster
        timestamp = date.datetime.now()
        previous_hash = previous_block.hash
        user = user
        new_block = Block(index, timestamp, previous_hash, user, monster_id, proof)
        self.chain.append(new_block)
        return self.chain

    def proof_of_work(self, prev_block):
        """."""
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


blockchain = BlockChain()












