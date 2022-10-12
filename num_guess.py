#!/usr/bin/env python3
# Created by: Frankie fox
# Created on: Oct 11, 2022
# This program checks the secret number 7
import constants

def main():
    # get numbers to guess 
    num_guess = int(input("Enter a number between 0 and 9: "))
    print()

    # check if the secret number was guessed
    if num_guess == constants.CORRECT_GUESS:
        print("You guessed right")

    # If the guess is wrong 
    if num_guess != constants.CORRECT_GUESS:
        print("You guessed wrong")

if __name__ == "__main__":
    main()

