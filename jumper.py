"""-Jumper (Teigen)
    For each life have associated line
    When tries reaches 4 guesses, game over
    Head turns to x when game over
    Return lines (diagram)"""

class Jumper:
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