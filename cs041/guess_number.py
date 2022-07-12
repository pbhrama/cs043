# This is a guess the number game.
import random

guessesTaken = 0
guessesToWin = int(input("Enter the number of guesses you think it will take for you to guess my number: "))

rangeNum = int(input("Enter the range of numbers you would like to guess from: "))

number = random.randint(1, rangeNum)
print('I am thinking of a number between 1 and ' + str(rangeNum) + '.')
print('You get ' + str(guessesToWin) + ' guesses!')

while guessesTaken < guessesToWin:
    print('Take a guess.')  # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')  # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
