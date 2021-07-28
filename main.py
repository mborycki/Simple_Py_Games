import guessing_game as g
import RockScissorsPaper as r
import hangman as h
import tic_tac_toe as t


print('Hello. Please choose a game:\n'
'Guessing Game for User: (A)\n'
'Guessing Game for Computer: (B)\n'
'Rock Scissors Paper: (C)\n'
'Hangman (D)\n'
'Tic Tac Toe (E)')

chosen_game = input('\nPlease type A \ B \ C \ D \ E: ').upper()

if chosen_game == 'A':
    g.user_guess(10)
elif chosen_game == 'B':
    name = input('Good choice. What is your name ')
    g.pc_guess(1,10,name)
elif chosen_game == 'C':
    r.rock_scissors_paper()
elif chosen_game == 'D':
    h.hangman_game(5)
elif chosen_game == 'E':
    t.tic_tac_toe_game()