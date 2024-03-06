import random


# define function
def guess_number():
    while True:
        # generate random integer
        secret_number = random.randint(1, 100)
        print(secret_number)

        count = 0  # count user attempts
        max_guesses = 10  # max number of guesses user has

        while count < max_guesses:
            try:
                user_guess = int(input("Guess a number between 1 and 100: "))

                # check if input number is out of range
                if user_guess > 100 or user_guess < 1:
                    print("please enter an integer between 1 and 100.\n")
                else:
                    count += 1

                    if user_guess < secret_number:
                        print(f"Your guess is too LOW. You have {max_guesses - count} tries left.\n")
                    elif user_guess > secret_number:
                        print(f"Your guess is too HIGH. You have {max_guesses - count} tries left.\n")
                    else:
                        print(f"Congratulations! You guessed in {count} attempts. The secret number is {secret_number}.\n")
                        break
            except ValueError:
                print("Please input an integer")
        else:
            print(f"Sorry you ran out of attempts. The secret number was {secret_number}\n")
        # restart game or quit
        restart_game = str(input("Do you want to play again? (Enter 'y' for yes, any other key to quit): "))
        if not restart_game.lower() == "y":
            print("Thanks for playing! Goodbye.")
            break


guess_number()

