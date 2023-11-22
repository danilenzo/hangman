import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self._choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def choose_random_word(self):
        return random.choice(self.word_list)

    def update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1

    def handle_correct_guess(self, guess):
        print(f"Good guess! '{guess}' is in the word.")
        self._update_word_guessed(guess)

    def handle_incorrect_guess(self, guess):
        self.num_lives -= 1
        print(f"Sorry, '{guess}' is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            self._handle_correct_guess(guess)
        else:
            self._handle_incorrect_guess(guess)

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self._check_guess(guess)
                self.list_of_guesses.append(guess)
            break

    def play_game(self):
        while True:
            if self.num_lives == 0:
                print("You lost!")
                break
            elif self.num_letters > 0:
                self.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                break


# You can add any words you like to the word_list
word_list = ['apple', 'banana', 'orange', 'tangerine', 'peach']
hangman_game = Hangman(word_list)
hangman_game.play_game()