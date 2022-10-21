import random

"""-List of words (Josiah)
    20 words (read a file idea)* or (convert strings to arrays character array)*
    randomly choose one
    return word to puzzle (use _ to make private)
"""
class Wordslist:
    

    def __init__(self):
        """Constructs a new Wordslist.

        Args:
            self (Wordslist): An instance of Wordslist.
        """
        self._words = ["charming", "perfect", "gorgeous", "gentle", "sleep", "rough",
        "sharp", "tasty", "cruel", "program", "thought", "drive", "accident", "accept", 
        "receive", "receipt", "random", "generate", "children", "charity"]
        #self._words = []
        #self._quantity = ""

    def rand_words(self):
        """This function will
    return one of these twenty words:
        
    Return: a randomly chosen word.
    """  
        
        word = random.choice(self._words)
        return word  


