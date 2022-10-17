"""Take player's letter guess from terminal service
        + Take word from word list
        + Compare letter guessed to word returned from list
        + Minus 1 life if letter guessed is not in word
            * Make list of letters already guessed

"""
import string

from words_list import Wordslist

class Puzzle:

    def compare_letter_to_word(self):

        # **list_of_words is a guess of what the word class is going to be named and get_valid_word for function/method
        word = Wordslist.get_valid_word(self)
        # making the word a iterable set
        word_letters = set(word) 
        # Set to uppercase and separate so letters can be accessed individually
        alphabet = set(string.ascii_uppercase)
        # Empty set that will be filled with player guesses
        player_set_of_guesses = set()  

        # Starting number of lives
        lives = 4
            
        # For continuation of play
        while len(word_letters) > 0 and lives > 0:
            # Letters used
            print('You have ', lives ,'more parachute strings and you have used these letters: ', ' '.join(player_set_of_guesses))

        # For current word
        word_list = [letter if letter in player_set_of_guesses else '-' for letter in word]
        # From Jumper class, print visual with number of lives left
        print(jumper.jumper_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        # **Input, not sure if this will be in this class
        player_guess = input('Guess a letter: ').upper()

        if player_guess in alphabet - player_set_of_guesses:
            # Add player guess to set
            player_set_of_guesses.add(player_guess)
            # Check if letter guessed in word
            if player_guess in word_letters:
                # Remove letter from the iterable set since it has been guessed
                word_letters.remove(player_guess)
                print('')

            else:
                # If wrong, -1 life/ parachute strings cut
                lives -= 1  
                print(f'\n{player_guess} is not in the word.')

        # Check if player_guess is already in the set of letters guessed
        elif player_guess in player_set_of_guesses:
            print(f'\n{player_guess} has been used. Guess another letter.')
        
        # If player enters something besides a single letter
        else:
            print(f'\nThat is not a valid letter.')

    # Check if there are any remaining lives, if not then end game.
    if lives == 0:
        # Show jumper with X for head
        print(jumper_visual_dict[lives])
        # Reveal word 
        print(f'Sorry, your parachute failed. The word was {word}.')
    else:
        # Reveal guessed word
        print(f'Terrific! You guessed {word}!')