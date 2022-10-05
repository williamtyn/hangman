import random

words = ['egg', 'thanks', 'problem', 'green', 'moving', 'history', 'camera', 'glasses', 'shower', 'jacket', 'popular', 'pumpkin']

def random_word(words):
    """
    Generates random word from list words.
    """
    word_random = random.choice(words).upper()
    return word_random

def letter_in_word(word):
    guess = input('Please input a letter/word between A - Z\n').upper()
    if (guess.isalpha()) == True:
        #lives -= 1
        #guessed_letters += guess
        return guess
    elif (guess.isalpha()) == True and guess == word:
        Print('Congrats! You guessed the right word')
    elif (guess.isalpha()) != True:
        print('Your guess can only contain letters A - Z, try again!\n')
    

def main():
    """
    Running main program
    """
    word = random_word(words)
    print('Welcome to Hangman Game!\n')
    letter_in_word(word)

main()