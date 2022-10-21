"""Take player's letter guess from terminal service
        + Take word from word list
        + Compare letter guessed to word returned from list
        + Minus 1 life if letter guessed is not in word
            * Make list of letters already guessed

"""
import string
# from .words_list import Wordslist
# from .jumper import Jumper

class Puzzle:
    def __init__(self):
        
        #self._jumper = Jumper()
        self._player_set_of_guesses = set()
        #self._word = Wordslist()
        self._lives = 4 
        self._alphabet = set(string.ascii_uppercase)
        self._word = ''
        

    def compare_letter_to_word(self, words_list):
        word = words_list.rand_words() 
         
        # working on this 
        self._word_letters = set(word) 
        #self.alphabet = set(string.ascii_uppercase)

        while len(self.word_letters) > 0 and self._lives > 0:
            print('You have ', self._lives ,'more parachute strings and you have used these letters: ', ' '.join(self._player_set_of_guesses))

        word_list = [letter if letter in self._player_set_of_guesses else '-' for letter in word]

        self._jumper.lines(self._lives)
        print('Current word: ', ' '.join(word_list))
        return word_list

    def player_input(self):
        player_guess = input('Guess a letter: ').upper()
        self.word_letters = set(self._word) 


        if player_guess in self._alphabet - self._player_set_of_guesses:
            self._player_set_of_guesses.add(player_guess)
            if player_guess in self.word_letters:
                self.word_letters.remove(player_guess)
                print('')

            else:
                self._lives -= 1  
                print(f'\n{player_guess} is not in the word.')

        elif player_guess in self._player_set_of_guesses:
            print(f'\n{player_guess} has been used. Guess another letter.')

        else:
            print(f'\nThat is not a valid letter.')

    def lives_left(self):
        if self._lives == 0:
            self._jumper.lines(self._lives)
            print(f'Sorry, your parachute failed. The word was {self._word}.')
        else:
            print(f'Terrific! You guessed {self._word}!')