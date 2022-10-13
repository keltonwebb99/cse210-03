# cse210-03
Here is the README.md to make the design for the project. Enter your name below when you are able to access:
Kelton Webb
Teigen Barber

Rules
Jumper is played according to the following rules:

The puzzle is a secret word randomly chosen from a list.
The player guesses a letter in the puzzle.
If the guess is correct, the letter is revealed.
If the guess is incorrect, a line is cut on the player's parachute.
If the puzzle is solved the game is over.
If the player has no more parachute the game is over.


Design

-List of words
    20 words (read a file idea)* or (convert strings to arrays character array)*
    randomly choose one
    return word to puzzle (use _ to make private)

-Puzzle
    take guess and compare with word
        Return lives (if true return correct position in array)


-Jumper
    For each life have associated line
    When tries reaches 4 guesses, game over
    Head turns to x when game over
    Display Word in "__ __"
    Return lines (diagram)


-Terminal_Service
    Makes a guess and returns to puzzle
        Input validation*
    Display altered jumper
    Display letters that have been guessed*
    Win/Lose method