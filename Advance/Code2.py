# Word Guessing Game

import random

def word_guess_game():
    words = ['python', 'apple', 'banana', 'orange', 'grape', 'mango']
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    print("Welcome to the Word Guess Game!")
    print(f"The word has {len(secret_word)} letters.")

    while attempts > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
        print("Word:", display_word)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
    else:
        print(f"Sorry, you ran out of attempts. The word was: {secret_word}")

if __name__ == "__main__":
    word_guess_game()
