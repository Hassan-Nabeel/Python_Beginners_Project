####    QUIZ GAME      ####

print('Welcome to the Quiz Game')
game = input('Do you want to play the game [Yes/No] : ').lower().strip()
if game != 'yes':
    print('Thank you')
    quit()
else:
    print('Lets start the game....')
print()
score = 0
answer1 = input('What do you mean by RAM ? : ').lower().strip()
if answer1 == 'random acess memory':
    print('Correct Answer !')
    score += 1
else:
    print('InCorrect Answer !')
print()
answer2 = input('What do you mean by ROM ? : ').lower().strip()
if answer2 == 'read only memory':
    print('Correct Answer !')
    score += 1
else:
    print('InCorrect Answer !')
print()
answer3 = input('What do you mean by MU ? : ').lower().strip()
if answer3 == 'memory unit':
    print('Correct Answer !')
    score += 1
else:
    print('InCorrect Answer !')
print()
answer4 = input('What do you mean by ML ? : ').lower().strip()
if answer4 == 'machine learning':
    print('Correct Answer !')
    score += 1
else:
    print('InCorrect Answer !')
print()
answer5 = input('What do you mean by DL ? : ').lower().strip()
if answer5 == 'deep learning':
    print('Correct Answer !')
    score += 1
else:
    print('InCorrect Answer !')
print()
print('You got ' + str(score) + ' correct answers.')
# print('You got',score,'correct answers.')


