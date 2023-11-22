import random

word_list = ['apple', 'banana', 'orange', 'tangerine', 'peach']

word = random.choice(word_list)

print(word)

guess = input("Enter a single alphabetical character: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")