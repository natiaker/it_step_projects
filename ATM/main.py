import random


class Account:
    def __init__(self, account_number, name, balance, pin):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.pin = pin

    def __str__(self):
        return (f"Account number: {self.account_number}, Name: {self.name}, Balance: {self.balance}, "
                f"PIN: {self.pin}")

    def check_balance(self):
        print(f"Balance: {self.balance}$")
        choose_action()

    def change_pin(self):
        new_pin = int(input("Enter the new pin (4 digits): "))
        if new_pin == self.pin:
            print("You are currently using this PIN")
        else:
            self.pin = new_pin
            print("PIN changed successfully")


def homepage():
    print("Create new account: 1")
    print("Login account: 2")
    home = int(input("Enter appropriate number: "))
    print()

    if home == 1:
        create_new_account()
    elif home == 2:
        login()
    else:
        print("Invalid")


def login():
    print("Login")
    enter_account_number = int(input("Enter your account number:"))
    pin = int(input("Enter your pin: "))
    choose_action()


def create_new_account():
    account_number = random.randint(10000, 99999)
    name = str(input("Enter your name: "))
    pin = int(input("Enter your pin: "))
    initial_balance = int(input("Enter your initial balance: "))

    account = Account(account_number, name, initial_balance, pin)
    user_list.append(account)
    print(f"Succesfully created account: {account}")
    for user in user_list:
        print(user)
    print()
    homepage()


def choose_action():
    print()
    print("Check Balance: 1")
    print("Deposit money: 2")
    print("Withdraw: 3")
    print("Change Pin: 4")
    print("Close account: 5")
    print("Log out: 6")
    num = int(input("Enter appropriate number: "))
    print()
    for user in user_list:
        if num == 1:
            user.check_balance()
        elif num == 2:
            print("deposit")
        elif num == 3:
            print("withdraw")
        elif num == 4:
            print("change pin")
        elif num == 5:
            print("close account")
        elif num == 6:
            print("loged out")
        else:
            print("Input number from 1 to 7")
            choose_action()

user_list = []

homepage()
