import guessing_game as gg
import RockScissorsPaper as rsp
import hangman

print('Hello. Please choose a game:\n'
'Guessing Game for User: (A)\n'
'Guessing Game for Computer: (B)\n'
'Rock Scissors Paper: (C)\n'
'Hangman (D)')
chosen_game = input('Please type A \ B \ C \ D: ').upper()

if chosen_game == 'A':
    gg.user_guess(10)
elif chosen_game == 'B':
    name = input('Good choice. What is your name ')
    gg.pc_guess(1,10,name)
elif chosen_game == 'C':
    rsp.rock_scissors_paper()
elif chosen_game == 'D':
    hangman.hangman_game(5)