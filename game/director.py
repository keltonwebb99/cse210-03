from game.puzzle import Puzzle
#from game.jumper import Jumper



class Director:
    def __init__(self):

        self._puzzle = Puzzle()
        self._is_playing = True
        #self._jumper = Jumper()
        # self._terminal_service = TerminalService()
        # self._lives = None
    def start_game(self):

        while self._is_playing:
            self._get_inputs()
         #   self._do_updates()
            self._do_outputs()
            self._end_game()

    def _get_inputs(self):
        # self._puzzle.player_input()
        self._puzzle.compare_letter_to_word()

   # def _do_updates(self):
    #    self._puzzle.lives_left()
        

    def _do_outputs(self):
        #self._jumper.lines(self._lives)
        
        # Will continue to run until game over
        self._puzzle.lives_left() 
        
        #if self._puzzle.lives_left._is_playing == False:
        #     print("game over")
        """If is playing is false then it will end game"""
        # self._end_game

    def _end_game(self):
        if self._puzzle._lives == 0:  
            self._is_playing = False
            print("game over")