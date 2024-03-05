import random


# define function
def guess_number():
    # generate random integer
    secret_number = random.randint(1, 100)
    print(secret_number)

    count = 0  # count user tries
    max_guesses = 10  # max number of guesses user has

    while count < max_guesses:
        try:
            user_guess = int(input("Guess the number - from 1 to 100: "))

            if user_guess > 100 or user_guess < 1:
                print("please enter an integer from 1 to 100\n")
            else:
                count += 1
                if user_guess < secret_number:
                    print(f"Your guess is too LOW. You have left {max_guesses - count} tries.\n")
                elif user_guess > secret_number:
                    print(f"Your guess is too HIGH. You have left {max_guesses - count} tries.\n")
                else:
                    print(f"Congratulations! You guessed in {count} try. The secret number is {secret_number}.")
                    return
        except ValueError:
            print("Please input a number")
    else:
        print(f"Sorry you lost. The secret number is {secret_number}")


guess_number()


