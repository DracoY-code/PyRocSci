import enum
import random

class MOVE(enum.Enum):
    Rock = 0
    Paper = 1
    Scissors = 2

print('Welcome to PyRocSci!')
print("We're gonna play Rock Paper Scissors with a high minded deity"
      + " greater than you. Let's see how well you do!\n")
print('- ROCK beats SCISSORS')
print('- SCISSORS beats PAPER')
print('- PAPER beats ROCK\n')

try:
    rounds = int(input('How many rounds are we looking forward to? '))
except ValueError or TypeError:
    print('Bad input! 😡')
    exit()

points = 0
min_win_req = rounds // 2

while rounds:
    usrch = input('\nChoose from [rock][paper][scissors] : ').capitalize()
    try:
        usrwgt = MOVE[usrch].value
    except KeyError:
        print('Broken input!')
        continue

    botch = random.choice(list(map(lambda x: x.name, MOVE)))
    print(f'Botty chose {botch}')
    botwgt = MOVE[botch].value

    win_status = False

    if usrwgt == botwgt:
        print("It's a tie!")
        continue
    elif usrwgt == 0 and botwgt == 2:
        win_status = True
    elif usrwgt == 1 and botwgt == 0:
        win_status = True
    elif usrwgt == 2 and botwgt == 1:
        win_status = True

    if win_status:
        print('You won the round!')
        points += 1
    else:
        print('You lost the round!')

    rounds -= 1

if points >= min_win_req:
    print('\nCongratulations! You won the game 😄')
else:
    print('\nYou lost bad! You should check in Grade 1 again 🤣')