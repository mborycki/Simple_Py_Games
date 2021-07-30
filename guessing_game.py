import random
from time import sleep
import os

clear = lambda: os.system('clear') # 'cls in Linux

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
    clear()
    print(f'Hi {name}. I will try to guess what is your number.')
    sleep(3)
    clear()
    print('Please choose your number within 5 seconds\n')
    sleep(5)
    
    answer = ''
    guess_counter = 0
    while answer != 'W':
        clear()
        guess_number = random.randint(min_no,max_no)
        if (guess_number - min_no) - (guess_number - max_no) == 0:
            answer = 'W'
        else:
            print(f'\nIs the number is {guess_number}:\n')
            answer = input(f"{name}'s answer (H - bigger, S - smaller, W - this is my number): ").upper()
            guess_counter += 1
            if answer == 'S':
                max_no = guess_number - 1
            elif answer == 'H':
                min_no = guess_number + 1
            else:
                print("I don't understand. Please type only: 'H', 'S', 'W'")
    clear()
    print(f'Hooray!!! I won :). Your number is {guess_number}. Anyway, I missed {guess_counter - 1} times.')
    sleep(5)
    clear()
    print(f'Thank you for your time.')
    

def user_guess(x):
    #x = int(input('Guessing Game\n.What is the maximum number?: '))
    guess_number = random.randint(1,x)
    print('The "guessing number" has been drawn.\n ')
    sleep(3)
    clear() 
    zero = 0
    guess_counter = 0
    while guess_number != zero:
        zero = int(input('\nPlease guess the number: '))
        if zero < guess_number:
            print('Nooo, the "guessing number" is higher...')
            sleep(2)
            guess_counter += 1
            clear() 
        elif zero > guess_number:
            print(f'Nooo, the "guessing number" is lower...')
            sleep(2)
            guess_counter += 1
            clear()
    print(f"Great!!! You won :). You missed {guess_counter} times")

