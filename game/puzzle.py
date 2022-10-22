
import string
from game.words_list import Wordslist
from game.jumper import Jumper


class Puzzle:
    """ Responsible for comparing player's letter guess with random word and return jumper.

    Attributes:
        jumper(str) : The game's jumper
        player_set_of_guesses(str) : make the word iterable
        words_list(str) : The game's wordlist 
        lives(int) = Number of lives at beginning of play 
        alphabet(str) = set of string
        new_word(str) = The generated word from Wordlist

    """
    def __init__(self):
        """Constructs Puzzle.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        
        self._jumper = Jumper()
        self._player_set_of_guesses = set()
        self._words_list = Wordslist()
        self._lives = 4 
        self._alphabet = set(string.ascii_lowercase)
        self.new_word = self._words_list.rand_words() 
        self._word_letters = set(self.new_word)

        # Uncomment next line for chosen word
        # print(self.new_word) 
        
    def compare_letter_to_word(self):

        # Checking for if more than 0 letters and more than 0 lives
        if len(self._word_letters) > 0 and self._lives > 0:
            print('You have ', self._lives ,'more parachute strings and you have used these letters: ', ' '.join(self._player_set_of_guesses))

        # what current word is (example: W - R D)
        word_list = [letter if letter in self._player_set_of_guesses else '-' for letter in self.new_word]

        # Prints # of lives jumper visual 
        self._jumper.lines(self._lives)

        print('Current word: ', ' '.join(word_list))

        # Get player guess
        player_guess = input('Guess a letter: ').lower()

        # Check if player_guess is in the word
        if player_guess in self._alphabet - self._player_set_of_guesses:
            # Add player guess to set
            self._player_set_of_guesses.add(player_guess)

            # Check if player_guess letter is in word
            if player_guess in self._word_letters:
                # Remove letter from the iterable set since it has been guessed
                self._word_letters.remove(player_guess)
                print('Terrific! You guessed right!')

            # If player guessed wrong
            else:
                # -1 life
                self._lives -= 1  
                print(f'\n{player_guess} is not in the word.')

        # Check if player_guess is already in the set of letters guessed
        elif player_guess in self._player_set_of_guesses:
            print(f'\n{player_guess} has been used. Guess another letter.')

        # If player enters something besides a single letter
        else:
            print(f'\nThat is not a valid letter.')

    def lives_left(self):
        # Check on number of lives. If 0 then end game, otherwise continue
        if self._lives == 0:
            self._jumper.lines(self._lives)
            # Reveal word 
            print(f'Sorry, your parachute failed. The word was {self.new_word}.')
            self.is_playing = False
            return self.is_playing
        else: return