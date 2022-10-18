from jumper import Jumper
from director import Director
class TerminalService:
    """This service will handle terminal operations"""

    """When called, this will prompt user to make a guess and return it"""
    def make_guess(self, player_guess):
        player_guess = input("Guess a letter: ").upper()
        return player_guess


    """Takes in the updated lines from jumper class and will dsiplay them when this function is called"""
    def display_jumper(self, new_jumper):
        new_jumper = Jumper.lines
        return new_jumper

#def display_guesses(self, guess_list):
        
    """When called, this will end game after _is_playing is False"""
    def game_over(self):
        print("GAME OVER")
        

