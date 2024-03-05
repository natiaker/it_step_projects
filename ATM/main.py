import random
import sys

from ATM.account import Account, AccountManager


# function for the homepage menu
# the user has the option to either log in or create a new account - using numbers.
def homepage(account_manager):
    while True:
        account_manager.write_accounts()  #
        print("Create new account: 1")
        print("Login account: 2")
        try:
            home = int(input("Enter appropriate number: "))
            print()
            if home == 1:
                create_new_account(account_manager)
            elif home == 2:
                login(account_manager)
            elif home == 3:
                sys.exit()  # exit loop and program
            else:
                print("Invalid number\n")
        except ValueError:
            print("Type numbers only\n")


# handle user login process. user should input account number and pin
def login(account_manager):
    while True:
        print("Input Login Info")
        account_number = str(input("Enter your account number: "))
        account = account_manager.check_account(account_number)  # check if account exists in account list
        pin = int(input("Enter your pin: "))
        # if account doesn't exist or pin doesn't match request the user to input valid data
        if account is None or not account.pin == pin:
            print("input valid account number or pin\n")
            break
        else:
            print("Login successful\n")
        choose_action(account_manager, account)  # navigate to user profile to choose actions


# create new account functionality
def create_new_account(account_manager):
    while True:
        print("Create new account")
        # generate unique account number for new user
        while True:
            account_number = str(random.randint(10000, 99999))
            if not account_manager.check_account(account_number):
                break  # Exit the loop if the account number is unique
            return account_number
        # request user to input name and pin
        name = str(input("Enter your name: "))
        pin = int(input("Enter your pin: "))
        initial_balance = 0
        print()
        # PIN code validation
        if not len(str(pin)) == 4:
            print("Invalid PIN. Please enter a 4-digit number.\n")
        else:
            account = Account(account_number, name, initial_balance, pin)  # create Account class object
            account_manager.add_account(account)  # add the newly created account to the list using the account manager
            print(f"Successfully created account: {account}\n")
        homepage(account_manager)


# function to choose actions for logged-in users
def choose_action(account_manager, account):
    while True:
        actions = """
Check Balance: 1
Deposit money: 2
Withdraw: 3
Change PIN: 4
Close account: 5
Log out: 6
Enter appropriate number: """
        try:
            num = int(input(actions))  # action number input
            print()
            # Conditional statement checks for the input number and executes corresponding actions
            if num == 1:
                print(f"Balance: {account.getbalance()}$")
            elif num == 2:
                amount = int(input("Enter the amount to deposit: "))
                account.deposit(amount)
                print(f"Balance: {account.getbalance()}$")
            elif num == 3:
                amount = int(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
                print(f"Balance: {account.getbalance()}$\n")
            elif num == 4:
                while True:
                    new_pin = int(input("Enter the new pin (4 digits): "))
                    if len(str(new_pin)) == 4 and str(new_pin).isdigit():  # check if the input pin is a 4 digit
                        if new_pin == account.get_pin():  # check if the new pin and old pin are the same
                            print(f"You already using this PIN")
                            break
                        account.change_pin(new_pin)
                        print("PIN changed successfully")
                        break
                    print("Invalid PIN. Please enter a 4-digit number.\n")
            elif num == 5:
                while True:
                    print("All your money will be withdrawn after entering PIN.")
                    print("To exit, please type '1'.")
                    pin = int(input("Enter your pin to close your account: "))
                    if pin == account.get_pin():
                        if account.getbalance() > 0:
                            print(f"Withdrawing money. Balance: {account.getbalance()}$")
                            account.withdraw(account.getbalance())
                        account_manager.delete_account(account)
                        print("Goodbye, successfully closed your account\n")
                        homepage(account_manager)
                        return
                    elif pin == 1:
                        break
                    else:
                        print("Invalid PIN\n")
            elif num == 6:
                homepage(account_manager)
            else:
                print("Input number from 1 to 6\n")
        # handle ValueError
        except ValueError:
            print("Invalid Value. Input numbers only\n")


# main function to start the program
def main():
    account_manager = AccountManager()  # create AccountManager class object
    account_manager.read_accounts()  # read json file
    homepage(account_manager)  # run homepage function


# checks whether the current script is being run as the main program, and if it is, it calls the main() function
if __name__ == "__main__":
    main()
