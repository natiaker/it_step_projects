import random



def choose_word():
    # List of words to choose from
    words = ["python", "hangman", "programming", "computer", "game", "player"]

    # Choose a random word from the list
    return random.choice(words)


def display_word(word, guessed_letters):
    # Display the word with dashes for letters not guessed
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    return display


def hangman():
    # Choose a word
    word = choose_word()

    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Try to guess the word. You have", attempts, "attempts.")


    while attempts > 0:
        # Display current state of the word
        print(display_word(word, guessed_letters))

        # Ask for a guess
        guess = input("Guess a letter: ").lower().strip()

        # Check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has been guessed already
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        print(guessed_letters)

        # Check if the guess is correct
        if guess not in word:
            attempts -= 1
            print("Incorrect! You have", attempts, "attempts left.")
        else:
            print("Correct!")

        # Check if the player has won
        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break

    # If no more attempts left
    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word)



# Start the game!
hangman()


