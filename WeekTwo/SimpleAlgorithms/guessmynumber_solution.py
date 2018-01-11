#!/bin/bsh/
# Be careful about the 'input command'. It should be used only for later input
# when user needs to answer with 'c', 'h' or 'l'.
# No need to write a command to take input for the guessed number from the
# user, just print a txt that will ask about the guessed number, like-
# print('Please think of a number between 0 and 100!')

low = 0
high = 100
print('Please think of a number between 0 and 100!')
while True:
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + ' ?')
    a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if a == 'c':
        print('Game over. Your secret number was:', str(guess))
        break
    elif a == 'l':
        low = guess
    elif a == 'h':
        high = guess
    else:
        print('Sorry, I did not understand your input.')
