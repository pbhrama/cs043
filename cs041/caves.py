import random
import time

char_name = print("What do you want your character's name to be?")


def player_name(name):
    name = input()
    return name


def displayIntro(name):
    print(name + ' is in a land full of dragons. In front of ' + name + ',')
    print(name + ' sees two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with' + name + '. The other dragon')
    print('is greedy and hungry, and will eat ' + name + ' on sight.')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('Which cave will he/she/it go into? (1, 2, or 3)')
        cave = input()

    return cave


def checkCave(chosenCave):
    print('He/she/it approaches the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of him/her/it! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 3)

    if chosenCave == str(friendlyCave):
        print('Gives he/she/it his treasure!')
    elif friendlyCave - 1 == 0 or friendlyCave - 1 == 2:
        print('Gobbles he/she/it down in one bite!')
    else:
        print('He sits there looking at him/her/it curiously and does nothing.')


real_name = player_name(char_name)
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    player_name(char_name)

    displayIntro(real_name)

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
