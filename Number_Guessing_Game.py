####        Number Guessing Game        ####

import random
print('Welcome to the Number Guessing Game ....')
print()
lower_range = int(input('Enter lower range number: '))
upper_range = int(input('Enter upper range number: '))
random_number = random.randint(lower_range,upper_range)
print()
print('Guess a number between',lower_range,'to',upper_range)
print()
count = 0
while True:
    count += 1
    guess = int(input('Enter the Number: '))
    if guess == random_number:
        print('You got it!')
        break
    elif guess > random_number:
        print('Guess a smaller number')
    else:
        print('Guess a greater number')
print()
print('You guessed in',count,'attempt!')
print()


