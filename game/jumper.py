
"""Outline Information from Week 5:
    -Jumper (Teigen)
    For each life have associated drawing
    When tries reaches 4 guesses, game over
    Head turns to x when game over
    print diagram from an if statement"""


class Jumper:
    #The job of the class is to provide visuals and print them in the terminal based on the 
    #number of lives the user has left. 

    #Attributes: just the lives count, which is brought in as a parameter rather than imported
    #Relationships: This class doesn't import anything, but is called on by the Puzzle class

    def _init_(self):
        #because I'm not importing other classes I don't need to initialize any variables. 
        #I just did the initialization to fit with the class syntax
        pass
        
        
    def lines(self, lives):
    #This method asks for two parameters, but when calling it you only need to include one in
    #the parentheses. The nature of self means that the method will grab the instance of self
    #just because I put it as a requirement in the parameters spot. Very interesting.
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