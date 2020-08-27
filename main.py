import datetime
from player import Player, Ticky

def winCheck(choice1: int, choice2: int) -> bool:
    """Returns the result of the round

    - choice1: int {choice of the first player}
    - choice2: int {choice of the second player}
    """
    return True if (
        choice1 == 0 and choice2 == 2
    ) or (
        choice1 == 1 and choice2 == 0
    ) or (
        choice1 == 2 and choice2 == 1
    ) else False

# Gimme your name
name = input('Please provide your name to continue : ')
player = Player(name)

print(f'\nWelcome to PyRocSci, {name}! 😃')

print(
    "We're gonna play everyone's favorite game, "
    + "'Rock Paper Scissors' with a high minded deity, "
    + "our friend Ticky! 🤖"
)

print(
    '\nYou might know the rules:' 
    + '\n* ROCK beats SCISSORS' 
    + '\n* SCISSORS beats PAPER'
    + '\n* PAPER beats ROCK'
)

# Number of rounds
try:
    rounds = int(input(f'\nHow many rounds can you handle, {name}? '))
except TypeError + ValueError:
    print('Bad input! 😡')
    exit()

# Must win this amount of rounds to be the champion
rounds_to_win = rounds // 2

ready = input('\nAre you ready [y/n]? ')

if ready == 'n':
    print('See you soon! ༼ つ ◕_◕ ༽つ')
    exit()

# Here is Ticky! 😄
ticky = Ticky()

while rounds:
    player_choice = player.choose()

    try:
        player_weight = player.get_weight(player_choice)
    except KeyError:
        print('Broken input! 🤕')
        continue

    # Ticky's choice
    ticky_choice = ticky.choose()
    ticky_weight = ticky.get_weight(ticky_choice)
    print(f'Ticky chose {ticky_choice}')

    # If you get a tie, not literally
    if player_choice == ticky_choice:
        print("It's a tie! ¯\_(ツ)_/¯")
        continue

    # Calculate result
    player_status = winCheck(player_weight, ticky_weight)

    # Result of the round
    if player_status:
        print('You won the round! 🎉')
        player.winner()
    else:
        print('You lost the round! 💩')

    rounds -= 1

if player.get_score() >= rounds_to_win:
    print('\nCongratulations! You won the game 😄')
    print('Your name will be registered in the hall of fame!')

    # Registering to hall of fame
    with open('hall_of_fame.md', 'a') as f:
        f.write(f'## {name} {datetime.datetime.now()}' + '\n')
else:
    print('\nToo bad! You lost 🙁')