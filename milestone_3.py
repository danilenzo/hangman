import random

secret_word = "apple"

def display_guess_result(guess, is_in_word):
    if is_in_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def normalize_guess(guess):
    return guess.lower()

def check_guess(guess):
    normalized_guess = normalize_guess(guess)
    is_in_word = normalized_guess in secret_word
    display_guess_result(normalized_guess, is_in_word)

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        check_guess(guess)
        break

ask_for_input()