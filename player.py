import enum
import random

class Move(enum.Enum):
    """ The possible choices in this game of death. """
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class Player:
    """ Main player class. """
    def __init__(self, name: str):
        self.name = name
        self.points = 0

    def choose(self):
        """Inputs the choice of the player
        """
        return input('\nChoose from [rock][paper][scissors] : ').upper()

    def get_weight(self, choice: str) -> int:
        """Returns the choice weight of the player

        - choice: str {The choice made by the player}
        """
        return Move[choice].value

    def winner(self) -> int:
        """Winner winner chicken dinner! 🐔 
        """
        self.points += 1
        return self.points

    def get_score(self) -> int:
        """Returns the score of the player
        """
        return self.points

class Ticky(Player):
    """ The Class for our friend Ticky. """
    def __init__(self):
        super().__init__(self)
        print("\nTicky says: Let's play!")

    def choose(self) -> str:
        """The exclusive choice of Mr. Ticky!
        """
        choice = random.choice(list(map(lambda x: x.name, Move)))
        return choice