import random
import os
import time

clear = lambda: os.system('clear')
def rock_scissors_paper():
    rsp_list = ['r','s','p']

    print("Welcome in the Rock Scissors Paper game.\n")

    while True:
        try:
            rounds_number = int(input("Please make a choice, how many times do you wanna play?: "))
        except:     
            clear()
            print("That was no valid number. Try again...")
            time.sleep(3)
            clear()
        else:
            break

    result_player = 0
    result_pc = 0
    print(f"Ok then, we will play {rounds_number} rounds.\nCurrent result is: Player: {result_player} | {result_pc} Computer")

    def game_result(player,computer):
        # r > s, s > p, p > r; if True then player won
        if player in rsp_list:
            if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
                return 'player'
            elif (player == 's' and computer == 'r') or (player == 'p' and computer == 's') or (player == 'r' and computer == 'p'):
                return 'computer'
            else:
                return 'tie'
        else:     
            return 'Wrong char'

    round_ = 1        
    while round_ <= rounds_number:
        clear()
        print(f"Result: Player - {result_player} | {result_pc} - Computer. Round {round_} of {rounds_number} \n")

        player_choice = input(f"Play: 'r' for rock, 's' for scissors, 'p' for paper: ").lower()
        computer_choice = random.choice(rsp_list)
        result = game_result(player_choice,computer_choice)

        if result == 'player':
            print(f'Player has got a point. {player_choice} > {computer_choice}')
            result_player += 1
            round_ += 1
            time.sleep(3)
        elif result == 'computer':
            print(f'Computer has got a point. {player_choice} < {computer_choice}')
            result_pc += 1
            round_ += 1
            time.sleep(3)
        elif result == 'tie':
            print(f'Tie. {player_choice} = {computer_choice}')
            round_ += 1
            time.sleep(3)
        else:
            clear()
            print("That was no valid character. Try again to use only those: 'r','s','p'")
            time.sleep(3)
            clear()

    clear()
    print(f"The final result: Player - {result_player} | {result_pc} - Computer\n")