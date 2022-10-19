from terminal_service import TerminalService
from puzzle import Puzzle
from jumper import Jumper



class Director:
    def __init__(self):
        
        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()

    def start_game(self):

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        new_guess = self._terminal_service.make_guess()
        self._puzzle.compare_letter_to_word(new_guess)

    def _do_updates(self):
        #Runs jumper class, returning updated jumper to terminal service
        pass

    def _do_ouputs(self):
        TerminalService.display_jumper(self)

        if self._jumper.dies: #the function that picks up if the dudes head is an x
            self._is_playing = False
        
        """If is playing is false then it will end game"""
        self._end_game

    def _end_game(self):
        if self._is_playing == False:
            TerminalService.game_over(self)