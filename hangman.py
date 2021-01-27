from words import hangman_words
import random
import string

def choose_a_word(hangman_words):
    word = random.choice(hangman_words)
    while '-' in hangman_words or ' ' in hangman_words: # we do not need spaces or dashes in our word
        word = random.choice(hangman_words)
    return word.upper()

word = choose_a_word(hangman_words)
word_letters = set(word)

alphabet = set(string.ascii_uppercase)

print(word)
print(word_letters)
print(alphabet)