"""."""
from django.conf import settings
from monsters.models import Monster
import monsters.scripts.stories as story
from django.core import serializers
import datetime as date
import hashlib
import json
from ..tasks import p_o_w


class Block(object):
    """Create a block that gets appended to our blockchain."""

    def __init__(self, index, timestamp, previous_hash, user, monster_data, proof):
        """Initialize each block."""
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.user = user
        self.monster_data = monster_data
        self.proof = proof
        self.hash = self._block_hash()

        self._update_chain()

    def _block_hash(self):
        """Hash all of the attributes for the current block."""
        sha = hashlib.sha256()
        index = str(self.index).encode('utf8')
        timestamp = str(self.timestamp).encode('utf8')
        previous_hash = str(self.previous_hash).encode('utf8')
        user = str(self.user).encode('utf8')
        monster_data = str(self.monster_data).encode('utf8')
        proof = str(self.proof).encode('utf8')
        sha.update(index +
                   timestamp +
                   previous_hash +
                   user +
                   monster_data +
                   proof)
        return sha.hexdigest()

    def view_block(self):
        """."""
        block = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'user': self.user,
            'monster_data': self.monster_data,
            'proof': self.proof,
            'hash': self.hash
        }, sort_keys=True, indent=4,
            separators=(',', ':'))
        return block

    def _update_chain(self):
        """."""
        block = {
            'index': self.index,
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'user': self.user,
            'monster_data': self.monster_data,
            'proof': self.proof,
            'hash': self.hash
        }
        if settings.DEBUG:
            with open('cryptomonsters/static/blockchain/blockchain.json') as file:
                chain = json.load(file)
            chain.append(block)
            with open('cryptomonsters/static/blockchain/blockchain.json', 'w') as file:
                json.dump(chain, file)
        else:
            with open(settings.STATIC_URL + 'blockchain/blockchain.json') as file:
                chain = json.load(file)
            chain.append(block)
            with open(settings.STATIC_URL + 'blockchain/blockchain.json', 'w') as file:
                json.dump(chain, file)


class BlockChain(object):
    """Blockchain that contains each block."""

    def __init__(self):
        """Initialize blockchain as list."""

        # Create genesis block on init.
        # genesis_block = Block(0, date.datetime.now().strftime("%c"), "0", "Genesis", 0, 0000)
        # self.chain.append(genesis_block)

    @property
    def chain(self):
        """."""
        with open('cryptomonsters/static/blockchain/blockchain.json') as file:
            chain = json.load(file)
        return chain

    def _get_previous_block(self):
        """Get the previous block in the chains."""
        return self.chain[-1]

    def new_block(self, user):
        """Add a new block to the chain."""
        previous_block = self._get_previous_block()
        ser_user = serializers.serialize('json', [user])
        proof_of_work = p_o_w.delay(previous_block, ser_user)
        async_id = (proof_of_work.as_tuple()[0][0])
        return async_id

    def _proof_of_work(self, prev_block, ser_user):
        """Run proof of work algorithm to mine to block."""
        previous_block = prev_block
        previous_block_index = previous_block['index']
        lead_zeros = 4
        nonce = 1
        proof_hash = self._calc_pow_hash(
            previous_block['index'], previous_block['timestamp'],
            previous_block['previous_hash'], previous_block['user'],
            previous_block['monster_data'], nonce)
        while str(proof_hash[0:lead_zeros]) != '0' * lead_zeros:
            check_previous_block = self._get_previous_block()
            if check_previous_block['index'] != previous_block_index:
                nonce = 0
                previous_block = check_previous_block
            nonce += 1
            proof_hash = self._calc_pow_hash(
                previous_block['index'], previous_block['timestamp'],
                previous_block['previous_hash'], previous_block['user'],
                previous_block['monster_data'], nonce)
        index = previous_block['index'] + 1
        des_user = serializers.deserialize('json', ser_user)
        user = next(des_user).object
        monster = create_monster(user)
        timestamp = date.datetime.now().strftime("%c")
        previous_hash = previous_block['hash']
        user = user.username
        monster_data = {
            'name': '{} the {}'.format(monster.name, monster.monster_type),
            'health': monster.health,
            'defense': monster.defense,
            'attack': monster.attack,
            'monster_type': monster.monster_type,
            'unique_id': monster.pk,
            'user': monster.user.username
        }
        new_block = Block(index, timestamp, previous_hash, user, monster_data, proof_hash)
        self.chain.append(new_block)
        return

    def _calc_pow_hash(self, index, timestamp, previous_hash, user, monster_data, nonce):
        """Calc new hash until the POW requirements are met."""
        sha = hashlib.sha256()
        index = str(index).encode('utf8')
        timestamp = str(timestamp).encode('utf8')
        previous_hash = str(previous_hash).encode('utf8')
        user = str(user).encode('utf8')
        monster_data = str(monster_data).encode('utf8')
        nonce = str(nonce).encode('utf8')
        sha.update(index +
                   timestamp +
                   previous_hash +
                   user +
                   monster_data +
                   nonce)
        return sha.hexdigest()


def create_monster(user):
    """."""
    types = {
        'Zombie': 'img/c_mon1.png',
        'Slime': 'img/c_mon2.png',
        'Skeleton': 'img/c_mon3.png',
        'Wolf': 'img/c_mon4.png',
        'Red Wizard': 'img/c_mon5.png',
        'Blue Wizard': 'img/c_mon6.png',
        'Bear': 'img/c_mon7.png',
        'Barbarian': 'img/c_mon8.png',
        'Minotaur': 'img/c_mon9.png',
        'Goblin': 'img/c_mon10.png',
    }
    monster = Monster()
    backstory = {
        'Zombie': story.zombie_story(monster.name),
        'Slime': story.slime_story(monster.name),
        'Skeleton': story.skeleton_story(monster.name),
        'Wolf': story.wolf_story(),
        'Red Wizard': story.wizard_story(monster.name),
        'Blue Wizard': story.wizard_story(monster.name),
        'Bear': story.bear_story(monster.name),
        'Barbarian': story.barbarian_story(monster.name),
        'Minotaur': story.minotaur_story(monster.name),
        'Goblin': story.goblin_story(monster.name),
    }
    monster.user = user
    monster.img_file = types[monster.monster_type]
    monster.monster_story = backstory[monster.monster_type]
    monster.save()
    monster.unique_id = monster.pk
    monster.save()
    return monster
