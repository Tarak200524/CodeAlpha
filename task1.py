import random

def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += "_"
    return displayed

def play_hangman():
    words = ["INDIA", "CHINA", "PAKISTAN", "THAILAND", "MALAYSIA", "BANGLADESH"]
    secret_word = random.choice(words)
    guessed_letters = []
    len_word=len(secret_word)
    attempts_left = len_word+2

    print("Welcome to Hangman!")
    print("Guess the word:", display_word(secret_word, guessed_letters))

    while attempts_left > 0:
        guess = input("Enter a letter: ").upper()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts_left -= 1
            print("Attempts left:", attempts_left)

            if attempts_left == 0:
                print("Game over\nThe word was:", secret_word)
                break

        displayed_word = display_word(secret_word, guessed_letters)
        print(displayed_word)

        if "_" not in displayed_word:
            print("Congratulations! You won")
            break
play_hangman()
