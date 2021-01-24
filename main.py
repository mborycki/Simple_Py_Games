import guessing_game as gg

print('Hello. Please choose a game:\n'
'Guessing Game for User: (A)\n'
'Guessing Game for Computer: (B)')
chosen_game = input('Please type A or B: ').upper()
if chosen_game == 'A':
    gg.user_guess(10)
elif chosen_game == 'B':
    name = input('Good choice. What is your name ')
    gg.pc_guess(1,10,name)