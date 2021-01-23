import random
import time

def pc_guess(min_no, max_no, name):
    '''
    In here I need to choose a number and keep it in my mind.
    PC will be guessing the number and my goal is to tell to PC 
    whether the guessed number is smaller ('S'), higher ('H') or if it won ('W').

    Atributes:
    min_no - begining number
    max_no - maximum number
    name - your name
    '''
    print(f'Hi {name} I will try to guess waht is your number. Please choose within 5 seconds a number.\n')
    time.sleep(5)
    answer = ''
    while answer != 'W':
        guess_number = random.randint(min_no,max_no)
        if (guess_number - min_no) - (guess_number - max_no) == 0:
            #print('Hooray!!! I won :)')
            answer = 'W'
        else:
            print(f'\nIs the number is {guess_number}:\n')
            answer = input(f"{name}'s number: ").upper()
            if answer == 'S':
                max_no = guess_number - 1
            elif answer == 'H':
                min_no = guess_number + 1
            elif answer == 'W':
                print(f'Hooray!!! I won :). Your number is {guess_number}')
            else:
                print("I don't understand. Please type only: 'H', 'S', 'W'")
    print(f'Hooray!!! I won :). Your number is {guess_number}')

def user_guess(x):
    #x = int(input('Guessing Game\n.What is the maximum number?: '))
    guess_number = random.randint(1,x)
    print("The guessing number has been draw.\n ")
    my_number = 0
    while guess_number != my_number:
        my_number = int(input('\nPlease type what is your number: '))
        if my_number < guess_number:
            print("Nooo, the Guessing Number is higher...")
        elif my_number > guess_number:
            print(f'Nooo, the Guessing Number is lower...')
    print("Great!!! You won :)")

print('Hello. Please choose a game:\n'
'Guessing Game for User: (A)\n'
'Guessing Game for Computer: (B)')
chosen_game = input('Please type A or B: ').upper()
if chosen_game == 'A':
    user_guess(10)
elif chosen_game == 'B':
    name = input('Good choice. What is your name ')
    pc_guess(1,10,name)