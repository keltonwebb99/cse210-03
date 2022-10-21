"""-Jumper (Teigen)
    For each life have associated drawing
    When tries reaches 4 guesses, game over
    Head turns to x when game over
    print diagram from an if statement"""

from game.puzzle import Puzzle

class Jumper:
    def _init_(self):
        self._puzzle= Puzzle()
        self._lives = self._puzzle.player_input
        

    def lines(self):
        if self._lives == 4:
            print("          /n"
                  "   ____   /n"
                  "  /    \  /n"
                  "   ____   /n"
                  "  \    /  /n"
                  "   \  /   /n"
                  "     O    /n"
                  "   / | \  /n"
                  "    / \   /n"
                  "          /n"
                  "^^^^^^^^^^/n")
        elif self._lives == 3:
            print("          /n"
                  "  /    \  /n"
                  "   ____   /n"
                  "  \    /  /n"
                  "   \  /   /n"
                  "     O    /n"
                  "   / | \  /n"
                  "    / \   /n"
                  "          /n"
                  "^^^^^^^^^^/n")
        elif self._lives == 2:
            print("          /n"
                  "  \    /  /n"
                  "   \  /   /n"
                  "     O    /n"
                  "   / | \  /n"
                  "    / \   /n"
                  "          /n"
                  "^^^^^^^^^^/n")
        elif self._lives == 1:
            print("          /n"
                  "   \  /   /n"
                  "     O    /n"
                  "   / | \  /n"
                  "    / \   /n"
                  "          /n"
                  "^^^^^^^^^^/n")
        elif self._lives == 0:
            print("          /n"
                  "     X    /n"
                  "   / | \  /n"
                  "    / \   /n"
                  "          /n"
                  "^^^^^^^^^^/n")