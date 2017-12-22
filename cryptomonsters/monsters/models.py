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
        names = ['Amy', 'Connor', 'Vanessa', 'Alex', 'Jordan', 'Frank', 'Chris', 'Natasha', 'Leah', 'Charlotte', 'Julie', 'Shawn', 'Alejandro', 'Shelby', 'Marvin', 'Sydney', 'Edward', 'Angela', 'Jeremiah', 'Austin', 'Miranda', 'Nathan', 'Abigail', 'Alexander', 'Luke', 'Lynn', 'Lisa', 'Kristine', 'Kathleen', 'Jacob', 'Keith', 'Jennifer', 'Anna', 'Thomas', 'Jaime', 'Jenny', 'Sheryl', 'Collin', 'Jodi', 'Melissa', 'Nicolas', 'Jorge', 'Jasmin', 'Jocelyn', 'Adrienne', 'Kathryn', 'Francisco', 'Roger', 'Allen', 'Craig', 'Shelly', 'Kayla', 'Michael', 'Lorraine', 'Mason', 'Steve', 'Valerie', 'Corey', 'Briana', 'Jackie', 'Shannon', 'Garrett', 'Jasmine', 'Samuel', 'Sara', 'Dale', 'Trevor', 'Mckenzie', 'Andrea', 'Diana', 'Barbara', 'Mariah', 'Janet', 'Rodney', 'Wanda', 'Rose', 'Erica', 'Andrew', 'Carlos', 'Tanya', 'Claudia', 'Jo', 'Cynthia', 'Christopher', 'Donald', 'Jesse', 'Dana', 'Sharon', 'Kaitlyn', 'Eugene', 'Jenna', 'Randall', 'Holly', 'Derek', 'Meghan', 'Megan', 'Caroline', 'Gabriela', 'Debra', 'Jeff', 'Nichole', 'Beverly', 'Evan', 'Pedro', 'Victoria', 'Scott', 'Joy', 'Whitney', 'William', 'Marc', 'Joe', 'Douglas', 'Miguel', 'Walter', 'Jason', 'Bethany', 'Crystal', 'Lindsay', 'Linda', 'Michele', 'Jack', 'Diane', 'Mandy', 'Sandra', 'Kyle', 'Jonathan', 'Brian', 'Patricia', 'Yvonne', 'Jeffrey', 'Noah', 'Casey', 'Claire', 'Steven', 'Joanne', 'Shelley', 'Jerry', 'Julia', 'Cassandra', 'Alicia', 'Angelica', 'Sue', 'Monica', 'Krista', 'Caitlin', 'Johnathan', 'Brett', 'Blake', 'Taylor', 'Tim', 'Christina', 'Suzanne', 'Glenn', 'Courtney', 'Alexandra', 'Dennis', 'Louis', 'Deanna', 'Colin', 'Stuart', 'Edgar', 'Evelyn', 'Maureen', 'Cody', 'Rebecca', 'Cristina', 'Donna', 'Derrick', 'Sherri', 'Vickie', 'Heather', 'Leon', 'Billy', 'Brandi', 'Alan', 'Debbie', 'Tina', 'Melvin', 'Cheryl', 'Don', 'Alexis', 'Laura', 'Curtis', 'Heidi', 'Amanda', 'Jacqueline', 'Ebony', 'Darrell', 'Ernest', 'Natalie', 'Colleen', 'Adam', 'Harold', 'Breanna', 'Emily', 'Brad', 'Ashley', 'Stanley', 'Dylan', 'Joyce', 'Dillon', 'Paula', 'John', 'Deborah', 'Rachael', 'Kara', 'Russell', 'Allison', 'Kristina', 'Ivan', 'Dan', 'Greg', 'Paul', 'Rachel', 'Jill', 'Sean', 'Tammie', 'Darren', 'Bruce', 'Autumn', 'Isabella', 'Devin', 'Hayley', 'Bryce', 'Ruth', 'Misty', 'Michaela', 'Daniel', 'Nina', 'Johnny', 'Brenda', 'Maria', 'Kelsey', 'Jamie', 'Frederick', 'Shaun', 'Danielle', 'Justin', 'Krystal', 'Zoe', 'Anthony', 'Gerald', 'Randy', 'Kimberly', 'Melanie', 'Darryl', 'Meredith', 'Erik', 'Ronnie', 'Amber', 'Chad', 'Reginald', 'Daisy', 'Kari', 'Lonnie', 'Lauren', 'Kristen', 'Jeanne', 'Brooke', 'April', 'Kevin', 'Mary', 'Christine', 'Margaret', 'Jesus', 'Elizabeth', 'Joann', 'Brittany', 'Lawrence', 'Ian', 'Nancy', 'Sandy', 'Phyllis', 'Roberto', 'Harry', 'Richard', 'Ellen', 'Lindsey', 'Alison', 'Tiffany', 'Bob', 'Howard', 'Ann', 'Samantha', 'Eric', 'Joel', 'Erin', 'Brianna', 'Stacy', 'Penny', 'Raymond', 'Dominique', 'Audrey', 'Cesar', 'Alyssa', 'Joseph', 'Ariel', 'Nicholas', 'Tracey', 'Carrie', 'Virginia', 'Laurie', 'Timothy', 'Robert', 'Susan', 'Kathy', 'Teresa', 'Pamela', 'Monique', 'Jose', 'Aaron', 'Nathaniel', 'Christian', 'Fernando', 'Ricky', 'Brandy', 'Madeline', 'Tom', 'Maurice', 'Martin', 'Kirsten', 'Beth', 'Ricardo', 'Travis', 'Dave', 'Darius', 'Barry', 'Victor', 'Yolanda', 'Gregory', 'Theresa', 'Joshua', 'Vincent', 'Mitchell', 'Michelle', 'Kristin', 'Brandon', 'David', 'Veronica', 'Melinda', 'Ethan', 'Bill', 'Joanna', 'Hannah', 'Candace', 'Sheri', 'Olivia', 'Wayne', 'Todd', 'Matthew', 'Arthur', 'Alexa', 'Wendy', 'Annette', 'Zachary', 'Charlene', 'Sierra', 'Kim', 'Patrick', 'Robin', 'Denise', 'Marcus', 'Carl', 'Henry', 'Cassidy', 'Troy', 'Gloria', 'Cathy', 'Kirk', 'Gail', 'Cory', 'Haley', 'Carol', 'Gina', 'Isaac', 'Peggy', 'Stephanie', 'Carolyn', 'Brent', 'Madison', 'Stephen', 'Faith', 'Kerri', 'Kelli', 'Clifford', 'Dwayne', 'Lee', 'Gary', 'Alexandria', 'Tracy', 'Bonnie', 'Wesley', 'Jay', 'Kenneth', 'Janice', 'Cindy', 'Lori', 'Loretta', 'Carly', 'Katie', 'Darlene', 'Kent', 'Danny', 'Katherine', 'Larry', 'Toni', 'Mia', 'Connie', 'Marissa', 'Gabriel', 'Jessica', 'Ronald', 'Kylie', 'Tara', 'Mark', 'Charles', 'Shelia', 'Erika', 'James', 'Renee', 'Antonio', 'Bryan', 'Helen', 'Mackenzie', 'Juan', 'Katelyn', 'Doris', 'Peter', 'Bradley', 'Karen', 'Jared', 'Roy', 'Philip', 'Molly', 'Latoya', 'Benjamin', 'Kristi', 'Tanner', 'Kaylee', 'Ariana', 'Mike', 'George', 'Luis', 'Tyler', 'Dean', 'Sheila', 'Rhonda', 'Vicki', 'Carla', 'Catherine', 'Jimmy', 'Shari', 'Dawn', 'Vernon', 'Dustin', 'Marie', 'Sarah', 'Tammy', 'Nicole', 'Julian', 'Kendra', 'Jeremy', 'Ryan', 'Melody', 'Kelly', 'Chelsea', 'Hailey']
        name = choice(names)
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
