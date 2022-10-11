import random  # import random library to random_word from words.py
from colorama import Fore, Style  # import library for print in colors
from words import words


HANGMAN = """
           +---+
           O   |
          /|\  |
          / \  |
              ===
          """

NICKNAME = ''


def choose_nickname():
    """
    As a player, you can choose your player nickname.
    """
    global nickname 
    choose_nick = input('Choose a nickname:')
    nickname = choose_nick
    print(f'Welcome {nickname}!\n')


def see_rules():
    """
    Players can choose to see the rules before entering the game.
    If a player doesn't want to see the rules, the game begins.
    """
    rules = input('Do you want to see the rules? Y/N\n').upper()
    if rules == 'Y':
        print('Hangman is a game of words '
              'where you guess the secret word as the computer shuffles them.')
        print('You can press any letter between A – Z to guess if that letter '
              'is in the word.')
        print('If you think you know the word,'
              'you can guess it by typing it in.')
        print('For each wrong word or letter,'
              'you will lose one of your lives.')
        print('You have 6 lives to guess the right word before it is '
              'Game Over!\n')


def random_word():
    """
    Generates random words from the list in words.py.
    """
    word_random = random.choice(words).upper()
    return word_random


def letter_in_word(word):
    """
    User input of letter/word and validating that input
    contains letter and nothing else.
    Returns True if the player guesses the right word.
    Returns False if the player is out of lives.

    Code enumerate source https://www.youtube.com/watch?v=m4nEnsavl6w&t=423s
    """
    lives = 3  # how many attempts the player have
    guessed_letters = []  # will display already guessed letters for player
    hidden_word = '_' * len(word)
    while lives > 0:
        print(word)
        print(f'Lives: {lives}')
        print("Guessed:", ' '.join(guessed_letters))
        print(hidden_word)
        guess = input('Please input a letter or word between A - Z\n').upper()
        if (guess.isalpha()) is True:
            if guess in word and guess == word:
                print(f'Congrats {nickname}, {guess} is the right word!')
                return True
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
            print('Your guess can only contain letters A - Z. Try again!\n')
    return False


def play_again():
    """
    Asks the player if they want to play again. If not, the program ends.
    """
    if input('Do you want to play again? Y/N\n').upper() == 'Y':
        return True
    else:
        return False


def game_loop():
    """
    Running the main program and functions.
    Loops the return so player can play again.
    If/elif of the return from letter_in_word to see what to print.
    """
    print('Welcome to Hangman Game!\n')
    print(hangman)
    choose_nickname()
    see_rules()
    game = True
    while game:
        word = random_word()
        gamestate = letter_in_word(word)
        if gamestate:
            win_game()
        elif not gamestate:
            game_over()
        game = play_again()


def game_over():
    """
    Prints the word 'Game Over' in asterisks and colours it red.
    """
    gameover = Fore.RED + """
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
                """
    print(gameover)
    print(Style.RESET_ALL)


def win_game():
    """
    Prints the word 'You Win' in asterisks and colours it green.
    """
    win = Fore.GREEN + """
            *    *   ****  *     *
             *  *   *    * *     *
              *     *    * *     *
              *     *    * *     *
              *      ****   *****

            *       *  ***  *    *  *
            *       *   *   * *  *  *
            *   *   *   *   *  * *  *
             * * * *    *   *   **
              *   *    ***  *    *  *
                """
    print(win)
    print(Style.RESET_ALL)


if __name__ == '__main__':
    game_loop()
