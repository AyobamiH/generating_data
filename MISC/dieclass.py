from random import randint

class Die:
    """A class representing a single die
    """
    # Initialize attribute
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

    # Roll Method

    def roll(self):
        return randint(1, self.num_sides)
