import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Initialize the Hangman game with a list of words and the number of lives
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def choose_random_word(self):
        # Choose a random word from the word list
        return random.choice(self.word_list)

    def update_word_guessed(self, guess):
        # Update the word_guessed list based on the correct guess
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1

    def handle_correct_guess(self, guess):
        # Handle a correct guess, updating the guessed word
        print(f"Good guess! '{guess}' is in the word.")
        self.update_word_guessed(guess)

    def handle_incorrect_guess(self, guess):
        # Handle an incorrect guess, decrement lives and provide feedback
        self.num_lives -= 1
        print(f"Sorry, '{guess}' is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def check_guess(self, guess):
        # Check if the guess is correct or incorrect and take appropriate actions
        guess = guess.lower()

        if guess in self.word:
            self.handle_correct_guess(guess)
        else:
            self.handle_incorrect_guess(guess)

    def ask_for_input(self):
        # Ask the player for a guess, handle invalid inputs and check the guess
        while True:
            guess = input("Guess a letter: ")

            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

            break  # For testing purposes

# Example usage:
hangman_game = Hangman(['apple', 'banana', 'orange'])
hangman_game.ask_for_input()
print(f"Updated word_guessed: {hangman_game.word_guessed}")
print(f"Remaining unique letters: {hangman_game.num_letters}")
print(f"Remaining lives: {hangman_game.num_lives}")