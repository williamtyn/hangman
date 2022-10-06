import random

words = ['egg', 'thanks', 'problem', 'green', 'moving', 'history', 'camera', 'glasses', 'shower', 'jacket', 'popular', 'pumpkin']

def random_word():
    """
    Generates random word from list words.
    """
    word_random = random.choice(words).upper()
    return word_random

def letter_in_word(word):
    """
    User input of letter/word and validating that input 
    contains letter and nothing else
    """
    lives = 6
    guessed_letters = []
    while lives > 0:
        print(word)
        print(f'You have {lives} lives left and have guessed {guessed_letters}\n')
        guess = input('Please input a letter/word between A - Z\n').upper()
        if (guess.isalpha()) == True:
            if guess in word:
                guessed_letters += guess
                print(guessed_letters)
            elif guess != word:
                lives -= 1
                guessed_letters += guess
                print(f'{lives} lives left')
                print(f'You have guessed {guessed_letters}')    
        elif (guess.isalpha()) != True:
            print('Your guess can only contain letters A - Z, try again!\n')
            break
    print('You lost the Game!')
            
    
def play_game():
    """
    Running main program
    """
    #lives = 6
    #guessed_letters = []
    word = random_word()
    print('Welcome to Hangman Game!\n')
    letter_in_word(word)


play_game()