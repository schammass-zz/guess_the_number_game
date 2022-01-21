# guess the number game
import random

print("**** WELCOME TO GUESS THE NUMBER !!!! ****")
print("**** You have 3 tries to guess the correct number! ****")
print("**** The range of numbers will be from 0-10 ****")

# variables to store winning number, user guess and number of tries
number = random.randint(0, 10)
guess = int(input("Please enter a positive integer number (0-10): "))
tries = 0

# check to see if the user guessed the right number
if guess == number:
    print("Congratulations you\'ve won!")

# noticed that you could input invalid numbers and it counted as a guess so this is how i solved that
while guess > 10 or guess < 0:
    guess = int(input("Please enter a VALID guess: "))
else:
    # my attempt at making the game loop
    while tries < 3 and guess != number:
        guess = int(input("Please guess again: "))
        tries = tries + 1
        # i noticed if i guessed the right answer out of the loop it would just exit so i duplicated here to prevent it
        if guess == number:
            print("Congratulations you\'ve won!")
        # implemented the lose mechanic
        elif tries == 3:
            print("You've Lost!")
        # same with the correct answer issue i had so i put it in the loop as well
        elif guess > 10 or guess < 0:
            while guess > 10 or guess < 0:
                guess = int(input("Please enter a VALID guess: "))
                # this is here because I didn't want to take tries away for invalid guesses
                tries = tries
