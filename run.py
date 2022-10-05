import random

words = ['problem', 'green', 'moving', 'history', 'camera', 'glasses', 'shower', 'jacket', 'popular', 'pumpkin']

def random_word(random):

    """
    Generates random word from list and loops trough the random word.
    """
    random = random.choice(words)
    for letter in random:
        print(letter)




def main():
    """
    Runs all program functions
    """
    random_word(random)

print('Welcome to my Hangman Game!')
main()
