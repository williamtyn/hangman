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
        #print(f'You have {lives} lives left and have guessed {guessed_letters}\n')
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
                print(f'{guess} is in the word')
            elif guess != word:
                lives -= 1
                guessed_letters += guess
                print(f'{guess} is NOT in the word')    
        elif (guess.isalpha()) == False:
            print('Your guess can only contain letters A - Z, try again!\n')
            break #will be removed before deployment
    print('End of game\n')

def play_again():
    play = input('Do you want to play again? Please press Y\n').upper()
    if play == 'Y':
        play_game()
    else break

def play_game():
    """
    Running main program
    """
    word = random_word()
    print('Welcome to Hangman Game!\n')
    letter_in_word(word)
    play_again()


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
 ')"""