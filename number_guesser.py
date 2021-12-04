# Beginner Project 1 - Number Guessing Game
# Given an upper and lower bound, the computer generates
# a number between said bounds, and the user is given a
# limited number of guesses depending on the bounds.

import random
import math


def number_game():

    # Getting inputs from user
    while True:
        lower = input("Enter Lower Bound: ")
        if lower.isnumeric():
            lower = int(lower)
            break
        print("\"{}\" is not a valid input!".format(lower))

    while True:
        upper = input("Enter Upper Bound: ")
        if upper.isnumeric():
            upper = int(upper)
            break
        print("\"{}\" is not a valid input!".format(upper))

    # Getting a random number between lower and upper bound
    x = random.randint(lower, upper)

    # Calculating number of guesses through log2(Upper bound – lower bound + 1)
    guesses = round(math.log((upper - lower + 1), 2))
    print("\nYou have {} guesses to guess the number I chose!\n".format(guesses))

    user_guesses = 0

    while user_guesses < guesses:
        guess = input("Enter your guess: ")

        user_guesses += 1

        if guess.isnumeric():
            guess = int(guess)
        else:
            print("\"{}\" is not a valid input! You have {} guesses left\n".format(
                guess, guesses - user_guesses))
            continue

        if guess < x:
            print("You guessed too low! You have {} guesses left\n".format(
                guesses - user_guesses))

        elif guess > x:
            print("You guessed too high! You have {} guesses left\n".format(
                guesses - user_guesses))

        else:
            print("Nice! You got it in {} tries!\n".format(user_guesses))
            return

    # If the users uses all their guesses, the number will be shown to them, and the game ends
    if user_guesses >= guesses:
        print("Better luck next time! The number was {}".format(x))
        return


if __name__ == "__main__":
    number_game()
