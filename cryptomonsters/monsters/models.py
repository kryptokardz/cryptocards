"""Moster model."""
from django.contrib.auth.models import User
from django.db import models
from faker import Faker
from random import choice
import itertools

fake = Faker()


def random_name():
    """Generate and return a randomized name."""
    whatever = [0, 1]
    if choice(whatever) == 0:
        beginning = ["Axe", "Glow", "Blade", "Blood", "Bone", "Cloud", "Crag", "Crest", "Doom", "Dream", "Coven", "Elf", "Fern", "Feather", "Fire", "Fist", "Flame", "Forest", "Hammer", "Heart", "Hell", "Leaf", "Light", "Moon", "Rage", "River", "Rock", "Shade", "Shadow", "Shield", "Snow", "Spirit", "Star", "Steel", "Stone", "Swift", "Tree", "Whisper", "Wind", "Wolf", "Wood", "Gloom", "Glory", "Orb", "Ash", "Blaze", "Amber", "Autumn", "Barley", "Battle", "Bear", "Black", "Blue", "Boulder", "Bright", "Bronze", "Burning", "Cask", "Chest", "Cinder", "Clan", "Claw", "Clear", "Cliff", "Cold", "Common", "Crystal", "Dark", "Dawn", "Day", "Dead", "Death", "Deep", "Dew", "Dirge", "Distant", "Down", "Dragon", "Dusk", "Dust", "Eagle", "Earth", "Ember", "Even", "Far", "Flat", "Flint", "Fog", "Fore", "Four", "Free", "Frost", "Frozen", "Full", "Fuse", "Gold", "Horse", "Gore", "Grand", "Gray", "Grass", "Great", "Green", "Grizzly", "Hallow", "Hallowed", "Hard", "Hawk", "Haze", "Heavy", "Haven", "High", "Hill", "Holy", "Honor", "Forest", "Humble", "Hydra", "Ice", "Iron", "Keen", "Laughing", "Lightning", "Lion", "Lone", "Long", "Low", "Luna", "Marble", "Meadow", "Mild", "Mirth", "Mist", "Molten", "Monster", "Morning", "Moss", "Mountain", "Moon", "Mourn", "Mourning", "Night", "Noble", "Nose", "Oat", "Ocean", "Pale", "Peace", "Phoenix", "Pine", "Plain", "Pride", "Proud", "Pyre", "Rain", "Rapid", "Raven", "Red", "Regal", "Rich", "Rose", "Rough", "Rumble", "Rune", "Sacred", "Sage", "Saur", "Sea", "Serpent", "Sharp", "Silent", "Silver", "Simple", "Single", "Skull", "Sky", "Slate", "Smart", "Snake", "Soft", "Solid", "Spider", "Spring", "Stag", "Star", "Stern", "Still", "Storm", "Stout", "Strong", "Summer", "Sun", "Tall", "Three", "Thunder", "Titan", "True", "Truth", "Marsh", "Tusk", "Twilight", "Two", "Void", "War", "Wheat", "Whit", "White", "Wild", "Winter", "Wise", "Wyvern", "Young", "Alpen", "Crest", "Crow", "Fallen", "Farrow", "Haven", "Master", "Nether", "Nickle", "Raven", "River", "Stone", "Tarren", "Terra", "Water", "Willow", "Wooden"]
        ending = ["axe", "glow", "beam", "blade", "blood", "bone", "cloud", "dane", "crag", "crest", "doom", "dream", "feather", "fire", "fist", "flame", "forest", "hammer", "heart", "hell", "leaf", "light", "moon", "rage", "river", "rock", "shade", "claw", "shadow", "shield", "snow", "spirit", "star", "steel", "stone", "swift", "tree", "whisper", "wind", "wolf", "wood", "gloom", "glory", "orb", "ash", "blaze", "arm", "arrow", "bane", "bash", "basher", "beard", "belly", "bend", "bender", "binder", "bleeder", "blight", "bloom", "blossom", "blower", "glade", "bluff", "bough", "bow", "brace", "braid", "branch", "brand", "breaker", "breath", "breeze", "brew", "bringer", "brook", "brow", "caller", "chaser", "reaper", "chewer", "cleaver", "creek", "crusher", "cut", "cutter", "dancer", "dew", "down", "draft", "dreamer", "drifter", "dust", "eye", "eyes", "fall", "fang", "flare", "flaw", "flayer", "flow", "follower", "flower", "force", "forge", "fury", "gaze", "gazer", "gem", "gleam", "glide", "grain", "grip", "grove", "guard", "gust", "hair", "hand", "helm", "hide", "horn", "hunter", "jumper", "keep", "keeper", "killer", "lance", "lash", "less", "mane", "mantle", "mark", "maul", "maw", "might", "more", "mourn", "oak", "ore", "peak", "pelt", "pike", "punch", "reaver", "rider", "ridge", "ripper", "roar", "run", "runner", "scar", "scream", "scribe", "seeker", "shaper", "shard", "shot", "shout", "singer", "sky", "slayer", "snarl", "snout", "soar", "song", "sorrow", "spark", "spear", "spell", "spire", "splitter", "sprinter", "stalker", "steam", "stream", "strength", "stride", "strider", "strike", "striker", "sun", "surge", "sword", "sworn", "tail", "taker", "talon", "thorn", "tide", "toe", "track", "trap", "trapper", "vale", "valor", "vigor", "walker", "ward", "watcher", "water", "weaver", "whirl", "whisk", "winds", "wing", "woods", "wound", "brooke", "fall", "fallow", "horn", "root", "shine", "swallow", "thorne", "willow", "wood"]
        name = choice(beginning) + choice(ending)
    else:
        fake = Faker()
        name = fake.first_name()
    return name


def random_stats():
    """Generate and return a randomized stat between 0 and 20."""
    first_digit = choice(list(itertools.chain([0 for _ in range(1, 14)], [1 for _ in range(14, 19)], [2])))
    if first_digit == 0:
        stat = first_digit + choice([x for x in range(1, 10)])
    elif first_digit == 1:
        stat = int(str(first_digit) + str(choice([x for x in range(10)])))
    else:
        stat = int(str(first_digit) + '0')
    return stat


def random_type():
    """Return type of monster."""
    types = (
        ('Slime'),
        ('Skeleton'),
        ('Zombie'),
        ('Blue Wizard'),
        ('Red Wizard'),
        ('Bear'),
        ('Wolf'),
        ('Barbarian'),
        ('Minotaur'),
        ('Goblin'),
        ('Ogre'),
    )
    return choice(types)


class Monster(models.Model):
    """Create new monster model."""

    user = models.ForeignKey(
        User,
        related_name='monsters',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default=random_name)
    health = models.IntegerField(default=random_stats)
    defense = models.IntegerField(default=random_stats)
    attack = models.IntegerField(default=random_stats)
    monster_type = models.CharField(max_length=100, default=random_type)
    unique_id = models.IntegerField(default=0)
    img_file = models.ImageField()
    monster_story = models.TextField(default='')

    def __str__(self):
        """Render as string."""
        return '{} the {}'.format(self.name, self.monster_type)
