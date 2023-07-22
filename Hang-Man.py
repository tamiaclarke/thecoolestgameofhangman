import random
import time

# welcoming the user
name = input("What is your name? ")
print ("Hello, " + name + ", time to play Hangman!")

# wait for 1 second
time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

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

    # ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # check if the letter has already been guessed
    if guess in guesses:
        print("You already guessed that letter.")
        continue

    # add the letter to the set of guesses
    guesses.add(guess)

    # check if the letter is in the word
    if guess in word:
        print("Good guess!")
    else:
        print("Sorry, that letter is not in the word.")
        # decrease the number of turns
        turns -= 1
        print(f"You have {turns} turns left.")

# check if the player lost
if turns == 0:
    print(f"Sorry, you lost. The word was {word}.")