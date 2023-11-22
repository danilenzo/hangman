import random

# Creating list of fruits
word_list = ['apple', 'banana', 'orange', 'tangerine', 'peach']

# Randomly chooses a fruit from a list
word = random.choice(word_list)

print(word)

guess = input("Enter a single alphabetical character: ")

# Checks if user input is alphabetical 
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")