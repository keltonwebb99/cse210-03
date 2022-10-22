from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): The game's puzzle.
        words_list: For generating random words to be used in the puzzle.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True
        
    def start_game(self):

        while self._is_playing:
            self._get_inputs()
            self._do_outputs()
            self._end_game()

    def _get_inputs(self):

        self._puzzle.compare_letter_to_word()

    def _do_outputs(self):
        
        # Will continue to run until game over
        self._puzzle.lives_left() 
        
        #if self._puzzle.lives_left() == False:
        #     print("Game Over. Thanks for playing!")
        # self._is_playing = False
        """If is playing is false then it will end game"""
        # self._end_game

    def _end_game(self):
        if self._puzzle._lives == 0:  
            self._is_playing = False
            print("Game Over")