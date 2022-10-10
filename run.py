import random  # import random library to random words from words.py
from words import words

hangman = ["""
           +---+
           O   |
          /|\  |
          / \  |
              ===
          """]

nickname = ''


def choose_nickname():
    """
    As a player you can choose your player nickname
    """
    global nickname 
    choose_nick = input('Choose a nickname:\n')
    nickname = choose_nick
    print(f'Welcome {nickname}!\n')


def see_rules():
    """
    Player can choose to see rules before entering the game
    """
    rules = input('Do you want to see the rules? Y/N\n').upper()
    if rules == 'Y':
        print('Hangman is game of words where you guess the secret word'
              'the computer shuffles.')
        print('You can press any letter between A – Z to guess if that letter'
              'is in the word.')
        print('If you think you know the word you can guess by typing it in.')
        print('For each wrong word or letter you will lose one of your lives.')
        print('You have 6 lives to guess the right word before it is'
              'Game Over!\n')
    else:
        play_game()


def random_word():
    """
    Generates random word from list words.
    """
    word_random = random.choice(words).upper()
    return word_random


def letter_in_word(word):
    """
    User input of letter/word and validating that input 
    contains letter and nothing else.

    Code enumerate source https://www.youtube.com/watch?v=m4nEnsavl6w&t=423s
    """
    lives = 3  # how many attempts the player have
    guessed_letters = []  # will display already guessed letters for player
    guessed = False
    hidden_word = '_' * len(word)
    while lives > 0 and guessed is False:
        print(word)
        print(f'Lives: {lives}') 
        print("Guessed:", ' '.join(guessed_letters))
        print(hidden_word)
        guess = input('Please input a letter/word between A - Z\n').upper()
        if (guess.isalpha()) is True:
            if guess in word and guess == word:
                print(f'Congrats {nickname}, {guess} is the right word')
                guessed = True
                break
            elif guess in word and guess not in guessed_letters:
                guessed_letters += guess
                show_letters = list(hidden_word)  
                ind = [i for i, letter in enumerate(word) if letter == guess]
                for index in ind:  # code to enumerate is of inspiration
                    show_letters[index] = guess  # from see docstring
                hidden_word = ''.join(show_letters)
            elif guess in guessed_letters:
                print(f'You have already guessed {guess}')
            elif guess != word:
                lives -= 1
                guessed_letters += guess  
        elif (guess.isalpha()) is False:
            print('Your guess can only contain letters A - Z, try again!\n')
    if lives == 0:
        print(f'Game over for you! {nickname}')  # add nickname variable and f-string
    else:
        print(f'Well played {nickname}!')


def play_again():
    """
    Ask player if they want to play again. If not the program ends.
    """
    play = input(f'Do you want to play again {nickname}? Y/N\n').upper()
    if play == 'Y':
        play_game()
    elif play == 'N':
        print('Thanks for playing Hangman!')
    else:
        print('Thanks for playing Hangman!')


def play_game():
    """
    Running main program
    """
    word = random_word()
    letter_in_word(word)


print('Welcome to Hangman Game!\n')
print(hangman)
choose_nickname()
see_rules()
play_game()
play_again()

"""
def game_over():
    print('
*****   ***  **  ** *****
*      *   * *  * * *
*  *** ***** *    * ***
*    * *   * *    * *
****** *   * *    * *****

 ****  *    *  ***** ****
*    * *    *  *     *   *
*    *  *  *   ***   ****
*    *  * *    *     * *
 ****    *     ***** *  *
 ')
print(game_over())
"""
"""
def win_game
*     *  ****  *     *
 *   *  *    * *     *
   *    *    * *     *
   *    *    * *     *
   *     ****   *****

*       *  ***  *    *  *
*       *   *   * *  *  *
*   *   *   *   *  * *  *
 * * * *    *   *   **  
  *   *    ***  *    *  *
"""


