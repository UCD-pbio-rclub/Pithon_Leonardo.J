#hangman

words = ['cat','dog','horse','elephant','wolf']
import random

lives_remaining = 15
guessed_letters = ' '


def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win!')
            break
        if lives_remaining == 0:
            print('You are Hung!')
            print('The word was: ' + word)
            break
            
def pick_a_word():
    return random.choice(words)

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining: ' + str(lives_remaining))
    guess = input(' Guess a letter or whole word?')
    return guess

def print_word_with_blanks(word):
    display_word= ' '
    for letter in word:
        if guessed_letters.find(letter) > -1:
            # letter found
            display_word = display_word + letter
        else:
            # letter not found
            display_word = display_word + '-'
    print(display_word)


def process_guess(guess, word):
    if len(guess) >= 3:
        return whole_word_guess(guess, word)
    if len(guess) == 1:
        return single_letter_guess(guess, word)
    if len(guess) > 1 and len(guess) != len(word):
        return False
    
def whole_word_guess(guess, word):
    global lives_remaining
    if guess == word:
        return True
    else:
        lives_remaining = lives_remaining - 1
        return False

def single_letter_guess(guess,word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        #world guess was incorrect
        lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):    
        return True

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
    return True





def print_word_with_blanks(word):
    display_word= ' '
    for letter in word:
        if guessed_letters.find(letter) > -1:
            # letter found
            display_word = display_word + letter
        else:
            # letter not found
            display_word = display_word + '-'
    print(display_word)
##    print('print_word_with_blanks:not done yet')

play()
    
