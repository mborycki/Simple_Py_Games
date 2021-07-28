from words import hangman_words
import random
import string
import os
from time import sleep

clear = lambda: os.system('clear')

def choose_a_word(hangman_words):
    word = random.choice(hangman_words)
    while '-' in word or ' ' in word: # we do not need spaces or dashes in our word
        word = random.choice(hangman_words)
    return word.upper()

def hangman_game(lives_number):
    '''
    Argument: lives = amount of lives you wanna have
    '''
    underline = ("\n-----------------------\n")
    clear()
    print("Welcome in the Hangman Game!" + underline)
    print('We are searching a word for you. Please wait a second...')
    lives = lives_number
    alphabet = set(string.ascii_uppercase)
    chosen_word = choose_a_word(hangman_words)
    word_letters = set(chosen_word)
    used_letters = set()
    missed_letters = list()
    sleep(5)

    while len(word_letters) > 0 and lives >= 1:
        clear()
        guessed_letters = [letter if letter in used_letters else "_" for letter in chosen_word]
        print(f"Remaining life: {lives}")
        print(f"Used letters: {missed_letters}")
        print("\nCurrent word: "," ".join(guessed_letters))
        user_letter = input("\nWrite a letter: ").upper()
        
        if user_letter in word_letters and user_letter in alphabet:
            clear()
            print(f"{underline}You guessed the letter: '{user_letter}'{underline}")
            sleep(3)
            word_letters.remove(user_letter)
            used_letters.add(user_letter)
        else:
            clear()
            print(f"{underline}Sorry try to guess another letter{underline}")
            sleep(3)
            missed_letters.append(user_letter)
            lives -= 1
    
    if lives == 0:
        clear()
        print(f"\n{underline}Sorry but you're dead. The chosen word was: '{chosen_word}'{underline}")
        sleep(3)
    else:
        clear()
        print(f"\n{underline}Congratulation! You guessed the chosen word was: '{chosen_word}'{underline}")
        sleep(3)