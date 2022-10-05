import random

words = ['egg','thanks','problem', 'green', 'moving', 'history', 'camera', 'glasses', 'shower', 'jacket', 'popular', 'pumpkin']

def random_word(words):

    """
    Generates random word from list words.
    """
    random = random.choice(words)
    print(random)


print('Welcome to Hangman game!')