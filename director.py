from terminal_service import TerminalService
from puzzle import Puzzle
from jumper import Jumper



class Director:
    def __init__(self):
        
        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        # self._terminal_service = TerminalService()
        self._lives = None
    def start_game(self):

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        self._puzzle.player_input()
        self._puzzle.compare_letter_to_word()

    def _do_updates(self):
        self._puzzle.lives_left()
        

    def _do_outputs(self):
        self._jumper.lines(self._lives)
        
        if self._jumper.lines == 0 #the function that picks up if the dudes head is an x
            self._is_playing = False
        
        """If is playing is false then it will end game"""
        self._end_game

    def _end_game(self):
        if self._is_playing == False:
            print("game over")