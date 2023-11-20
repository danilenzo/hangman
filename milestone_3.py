import random

secret_word = "peach"

def check_guess(guess):
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        check_guess(guess)
        break

ask_for_input()