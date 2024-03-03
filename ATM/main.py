import random

from ATM.account import Account, AccountManager


def homepage(account_manager):
    while True:
        account_manager.write_accounts()
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
                return
            else:
                print("Invalid number\n")
        except ValueError:
            print("Type numbers only\n")


def login(account_manager):
    while True:
        print("Input Login Info")
        account_number = str(input("Enter your account number: "))
        account = account_manager.check_account(account_number)
        pin = int(input("Enter your pin: "))
        if account is None or not account.pin == pin:
            print("input valid account number or pin\n")
            break
        else:
            print("Login successful\n")
        choose_action(account_manager, account)


def create_new_account(account_manager):
    while True:
        print("Create new account")

        while True:
            account_number = str(random.randint(10000, 99999))
            if not account_manager.check_account(account_number):
                break  # Exit the loop if the account number is unique
            return account_number

        name = str(input("Enter your name: "))
        pin = int(input("Enter your pin: "))
        initial_balance = 0
        print()

        if not len(str(pin)) == 4:
            print("Invalid PIN. Please enter a 4-digit number.\n")
            continue
        else:
            account = Account(account_number, name, initial_balance, pin)
            account_manager.add_account(account)
            print(f"Successfully created account: {account}\n")
        homepage(account_manager)


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
            num = int(input(actions))
            print()

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
                    if len(str(new_pin)) == 4 and str(new_pin).isdigit():
                        if new_pin == account.get_pin():
                            print(f"You already using this PIN")
                            break
                        account.change_pin(new_pin)
                        print("PIN changed successfully")
                        break
                    print("Invalid PIN. Please enter a 4-digit number.\n")
            elif num == 5:
                while True:
                    print("All your money will be withdrawn after entering PIN.")
                    print("ENTER 1 to quit")
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
        except ValueError:
            print("Invalid Value. Input numbers only")


def main():
    account_manager = AccountManager()
    account_manager.read_accounts()
    homepage(account_manager)


if __name__ == "__main__":
    main()
