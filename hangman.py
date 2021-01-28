from words import hangman_words
import random
import string

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
    lives = lives_number
    alphabet = set(string.ascii_uppercase)
    chosen_word = choose_a_word(hangman_words)
    word_letters = set(chosen_word)
    used_letters = set()
    print(f"Word: {chosen_word}\n")
    
    while len(word_letters) > 0 and lives >= 1:
        guessed_letters = [letter if letter in used_letters else "_" for letter in chosen_word]
        print(f"Remaining life: {lives}")
        print("\nCurrent word: "," ".join(guessed_letters))
        user_letter = input("\nWrite a letter: ").upper()
        
        if user_letter in word_letters and user_letter in alphabet:
            print(f"{underline}You guessed the letter: '{user_letter}'{underline}")
            word_letters.remove(user_letter)
            used_letters.add(user_letter)
        else:
            print(f"{underline}Sorry try to guess another letter{underline}")
            lives -= 1
    
    if lives == 0:
        print(f"\n{underline}Sorry but you're dead. The chosen word was: '{chosen_word}'{underline}")
    else:
        print(f"\n{underline}Congratulation! You guessed the chosen word was: '{chosen_word}'{underline}")