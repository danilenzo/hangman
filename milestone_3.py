import random

# The secret word that the player needs to guess
secret_word = "apple"

# Function to display the result of a guess
def display_guess_result(guess, is_in_word):
    if is_in_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Please try again.")

# Function to normalize the guess (convert to lowercase)
def normalize_guess(guess):
    return guess.lower()

# Function to check if the guess is in the secret word and display the result
def check_guess(guess):
    normalized_guess = normalize_guess(guess)
    is_in_word = normalized_guess in secret_word
    display_guess_result(normalized_guess, is_in_word)

# Function to get the player's guess and check it
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        check_guess(guess)
        break  # This break statement will exit the loop after the first iteration

# Call the function to start the game
ask_for_input()