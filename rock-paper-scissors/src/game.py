import random
class RockPaperScissors:
    def __init__(self):
        # Constructor method
        # Initialize game settings
        self.choices = ['rock', 'paper', 'scissors']

    def validate_choice(self, player_choice):
        # Check if choice is valid
        if player_choice not in self.choices:
            return False
        return True