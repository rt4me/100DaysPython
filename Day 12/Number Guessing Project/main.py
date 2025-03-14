from art import logo
import random

NUM_TO_GUESS = random.randint(1,100)
TURNS_FOR_HARD_DIFFICULTY = 5
TURNS_FOR_EASY_DIFFICULTY = 10

def guess_the_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        tries = TURNS_FOR_EASY_DIFFICULTY
    else:
        tries = TURNS_FOR_HARD_DIFFICULTY

    while tries > 0:
        guess = int(input("Make a guess: "))
        if guess == NUM_TO_GUESS:
            print(f"You got it! The answer was {NUM_TO_GUESS}")
            return
        elif guess > NUM_TO_GUESS:
            print("Too high.")
        elif guess < NUM_TO_GUESS:
            print("Too low.")
        tries -= 1
        if tries > 0:
            print("Guess again.")
            print(f"You have {tries} attempts remaining to guess the number")

    if tries <= 0:
        print("You've run out of guesses.")
        print(f"The number was {NUM_TO_GUESS}.")

guess_the_number()