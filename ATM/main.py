import json
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
        choose_action(self)

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
        write_accounts()
        print(f"Balance: {self.balance}$")
        choose_action(self)

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        self.balance -= amount
        write_accounts()
        print(f"Balance: {self.balance}$")
        choose_action(self)

    def change_pin(self):
        new_pin = int(input("Enter the new pin (4 digits): "))
        if new_pin == self.pin:
            print("You are currently using this PIN")
        else:
            self.pin = new_pin
            write_accounts()
            print("PIN changed successfully")
        choose_action(self)

    def close_account(self):
        while True:
            if self.balance > 0:
                print(f"Withdraw money before closing your account. Balance: {self.balance}$")
                self.withdraw()
            else:
                pin = int(input("Enter your pin to close your account: "))
                if pin == self.pin:
                    user_list.remove(self)
                    write_accounts()
                    print("Goodbye, successfully closed your account\n")
                    homepage()
                    return
                else:
                    print("Invalid PIN\n")

    def logout(self):
        print("You have been logged out")
        homepage()


def serialization_func(obj):
    if isinstance(obj, Account):
        return {"account_number": obj.account_number, "name": obj.name, "balance": obj.balance, "pin": obj.pin}
    raise TypeError(f'Not type of Account')


def write_accounts():
    with open('accounts.json', 'w') as json_file:
        json.dump(user_list, json_file, default=serialization_func, indent=4)


def deserialization_func(obj):
    return Account(obj["account_number"], obj["name"], obj["balance"], obj["pin"])


def read_accounts():
    with open('accounts.json', 'r') as json_file:
        new_user_list = json.load(json_file, object_hook=deserialization_func)
        return new_user_list


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
    while True:
        print("Input Login Info")
        account_number = str(input("Enter your account number: "))
        pin = int(input("Enter your pin: "))
        print()
        for user in user_list:
            if account_number == user.account_number and pin == user.pin:
                print("Login Successfully")
                choose_action(user)
                return
        print("input valid account number and pin\n")


def create_new_account():
    print("create new account")
    account_number = str(random.randint(10000, 99999))
    name = str(input("Enter your name: "))
    pin = int(input("Enter your pin: "))
    initial_balance = int(input("Enter your initial balance: "))
    print()

    account = Account(account_number, name, initial_balance, pin)
    user_list.append(account)
    write_accounts()
    print(f"Successfully created account: {account}")
    print("User list: ")
    for user in user_list:
        print(user)
    print()
    homepage()


def choose_action(account):
    print()
    print("Check Balance: 1")
    print("Deposit money: 2")
    print("Withdraw: 3")
    print("Change Pin: 4")
    print("Close account: 5")
    print("Log out: 6")
    num = int(input("Enter appropriate number: "))
    print()

    if num == 1:
        account.check_balance()
    elif num == 2:
        account.deposit()
    elif num == 3:
        account.withdraw()
    elif num == 4:
        account.change_pin()
    elif num == 5:
        account.close_account()
    elif num == 6:
        account.logout()
    else:
        print("Input number from 1 to 7")
        choose_action(account)


user_list = read_accounts()

homepage()

