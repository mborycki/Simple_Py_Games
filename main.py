import guessing_game as g
import RockScissorsPaper as r
import hangman as h
import tic_tac_toe as t
import os

clear = lambda: os.system('clear') 

print('\nHello. Please choose a game:\n'
'Guessing Game for User: (A)\n'
'Guessing Game for Computer: (B)\n'
'Rock Scissors Paper: (C)\n'
'Hangman (D)\n'
'Tic Tac Toe (E)')

chosen_game = input('\nPlease type A \ B \ C \ D \ E: ').upper()

if chosen_game == 'A':
    clear()
    print('Your goal is to guess a number between 1 and 10')
    g.user_guess(10)
elif chosen_game == 'B':
    clear()
    name = input('Hello. What is your name?\n>> ')
    g.pc_guess(1,10,name)
elif chosen_game == 'C':
    r.rock_scissors_paper()
elif chosen_game == 'D':
    h.hangman_game(5)
elif chosen_game == 'E':
    t.tic_tac_toe_game()