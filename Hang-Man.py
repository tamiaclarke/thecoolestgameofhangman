import random
import time

def hangman_game():
    # select a random word from a list
    words = ['chocolate', 'caramel', 'strawberries', 'cupcakes', 'cake']
    word = random.choice(words)

    # create a variable to store the guesses
    guesses = set()

    # determine the number of turns
    turns = 10

    # create a while loop
    while turns > 0:
        # print the current status of the word
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
        print("")  # add a newline

        # check if all the letters have been guessed
        if set(word) == guesses:
            print("Congratulations, you won!")
            break

        # ask the user to guess a letter or get a hint
        guess = input("Guess a letter or type 'hint' for a hint: ").lower()

        # check if the letter has already been guessed
        if guess in guesses:
            print("You already guessed that letter.")
            continue

        # handle the hint feature
        if guess == "hint":
            hidden = [char for char in word if char not in guesses]
            hint = random.choice(hidden)
            print("Hint: One of the letters is:", hint)
            continue

        # add the letter to the set of guesses
        guesses.add(guess)

        # check if the letter is in the word
        if guess in word:
            print("Good guess!")
        else:
           
