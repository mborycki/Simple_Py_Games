import guessing_game as gg
import RockScissorsPaper as rsp

print('Hello. Please choose a game:\n'
'Guessing Game for User: (A)\n'
'Guessing Game for Computer: (B)\n'
'Rock Scissors Paper: (C)')
chosen_game = input('Please type A \ B \ C: ').upper()

if chosen_game == 'A':
    gg.user_guess(10)
elif chosen_game == 'B':
    name = input('Good choice. What is your name ')
    gg.pc_guess(1,10,name)
elif chosen_game == 'C':
    rsp.rock_scissors_paper()