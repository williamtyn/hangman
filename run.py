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
    contains letter and nothing else.
    """
    lives = 6 #how many attempts the player have
    guessed_letters = [] #will display already guessed letters for player
    guessed = False
    hidden_word = '_' * len(word)
    while lives > 0:
        print(word)
        print(hidden_word)
        print(f'You have {lives} lives left and have guessed {guessed_letters}\n')
        guess = input('Please input a letter/word between A - Z\n').upper()
        if (guess.isalpha()) == True:
            if guess in word and guess == word:
                print(f'Gongrats, {guess} is the right word')
                break
            elif guess in word:
                guessed_letters += guess
                show_letters = list(hidden_word) #code to enumerate is inspiration from https://www.youtube.com/watch?v=m4nEnsavl6w&t=423s
                indices = [i for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    show_letters[index] = guess
                hidden_word = ''.join(show_letters)
                if '_' not in hidden_word:
                    guessed = True 
                print(f'{guess} is in the word\n')
            elif guess != word:
                lives -= 1
                guessed_letters += guess
                print(f'{guess} is NOT in the word\n')    
        elif (guess.isalpha()) == False:
            print('Your guess can only contain letters A - Z, try again!\n')
    print('End of game\n')


def play_again():
    """
    Ask player if they want to play again. If not the program ends.
    """
    play = input('Do you want to play again? Please press Y\n').upper()
    if play == 'Y':
        play_game()
    else:
        print('Thanks for playing Hangman!')

def see_rules():
    rules = input('Do you want to see the rules? Y/N\n').upper()
    if rules == 'Y':
        print('Hangman is game of words where you guess the secret word the computer shuffles.\nYou can press any letter between A – Z to guess if that letter is in the word.\nIf you think you know the word you can guess by typing it in.\nFor each wrong word or letter you will lose one of your lives.\nYou have 6 lives to guess the right word before it is Game Over!\n')
    else:
        play_game()

def play_game():
    """
    Running main program
    """
    word = random_word()
    letter_in_word(word)
    play_again()

print('Welcome to Hangman Game!\n')
see_rules()
play_game()

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