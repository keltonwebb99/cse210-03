"""-Jumper (Teigen)
    For each life have associated drawing
    When tries reaches 4 guesses, game over
    Head turns to x when game over
    print diagram from an if statement"""

#from game.puzzle import Puzzle

class Jumper:

    def _init_(self):
        self._lives = self._puzzle.player_input
        

    def lines(self, lives):
        if lives == 4:
            print("          \n"
                  "   ____   \n"
                  "  /    \  \n"
                  "   ____   \n"
                  "  \    /  \n"
                  "   \  /   \n"
                  "     O    \n"
                  "   / | \  \n"
                  "    / \   \n"
                  "          \n"
                  "^^^^^^^^^^\n")
        elif lives == 3:
            print("          \n"
                  "  /    \  \n"
                  "   ____   \n"
                  "  \    /  \n"
                  "   \  /   \n"
                  "     O    \n"
                  "   / | \  \n"
                  "    / \   \n"
                  "          \n"
                  "^^^^^^^^^^\n")
        elif lives == 2:
            print("          \n"
                  "  \    /  \n"
                  "   \  /   \n"
                  "     O    \n"
                  "   / | \  \n"
                  "    / \   \n"
                  "          \n"
                  "^^^^^^^^^^\n")
        elif lives == 1:
            print("          \n"
                  "   \  /   \n"
                  "     O    \n"
                  "   / | \  \n"
                  "    / \   \n"
                  "          \n"
                  "^^^^^^^^^^\n")
        elif lives == 0:
            print("          \n"
                  "     X    \n"
                  "   / | \  \n"
                  "    / \   \n"
                  "          \n"
                  "^^^^^^^^^^\n")