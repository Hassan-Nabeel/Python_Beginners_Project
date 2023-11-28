####        Rock - Paper - Scissor        ####

import random
print('Welcome to the Rock - Paper - Scissor Game ....')
user_win = 0
comp_win = 0
option = ['rock','paper','scissor']

while True:
    print()
    user_input =input('Enter Rock/Paper/Scissor or Q to Quit: ').lower().strip()
    if user_input == 'q':
        break
    elif user_input not in option:
        print('Enter a valid option')
        continue

    random_number = random.randint(0,2)         # rock: 0, paper: 1, scissor: 2
    computer_pick = option[random_number]
    print('Computer picked:',computer_pick)

    if user_input == 'rock' and computer_pick == 'scissor':
        print('You Won!')
        user_win += 1

    elif user_input == 'paper' and computer_pick == 'rock':
        print('You Won!')
        user_win += 1
        
    elif user_input == 'scissor' and computer_pick == 'paper':
        print('You Won!')
        user_win += 1
    
    elif user_input == 'rock' and computer_pick == 'rock':
        print('Draw!')
      
    elif user_input == 'paper' and computer_pick == 'paper':
        print('Draw!')

    elif user_input == 'scissor' and computer_pick == 'scissor':
        print('Draw!')

    else:
        print('You Lost!')
        comp_win += 1


print("You won", user_win, "times.")
print("The computer won", comp_win, "times.")
print("Goodbye!")



