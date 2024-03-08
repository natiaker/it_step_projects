import json
import random

ACCOUNT_FILE = "accounts.json"


# define Account class
class Account:
    # Initialize an Account object with account number, name, balance and pin
    def __init__(self, account_number, name, balance, pin):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.pin = pin

    # return a string representation of Account object
    def __str__(self):
        return (f"Account number: {self.account_number}, Name: {self.name}, Balance: {self.balance}, "
                f"PIN: {self.pin}")

    # get the current balance of the account
    def getbalance(self):
        return self.balance

    # get the account number
    def get_account_number(self):
        return self.account_number

    # deposit specified amount of money into the balance
    # check deposit amount to be greater than 0
    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
        else:
            self.balance += amount

    # withdraw specified amount of money from balance
    # check the amount to be greater than 0 and check if there is enough money on balance to withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
        elif self.balance < amount:
            print("Not enough money")
        else:
            self.balance -= amount

    # change pin with new pin
    def change_pin(self, pin):
        self.pin = pin

    # return current pin
    def get_pin(self):
        return self.pin


# custom serialization method to translate Account class into json format
def serialization_func(obj):
    # check if the object is an Account class type
    if isinstance(obj, Account):
        return {"account_number": obj.account_number, "name": obj.name, "balance": obj.balance, "pin": obj.pin}
    raise TypeError(f'Not type of Account')


# custom deserialization method to translate json file into Account class instance
def deserialization_func(obj):
    return Account(obj["account_number"], obj["name"], obj["balance"], obj["pin"])


# define account manager class
class AccountManager:
    # initialize empty account list
    def __init__(self):
        self.account_list = []

    # write accounts in json file using custom deserialization method
    def write_accounts(self):
        with open(ACCOUNT_FILE, 'w') as json_file:
            json.dump(self.account_list, json_file, default=serialization_func, indent=4)

    # read accounts from json file and save it in account_list
    def read_accounts(self):
        with open(ACCOUNT_FILE, 'r') as json_file:
            new_account_list = json.load(json_file, object_hook=deserialization_func)
        self.account_list = new_account_list

    # method to append user input account to the account list
    def add_account(self, account):
        self.account_list.append(account)

    # check if the user input account exists in the account list
    def check_account(self, account_number):
        for account in self.account_list:
            if account.get_account_number() == account_number:
                return account
        return None

    # method to remove specified account from the account list
    def delete_account(self, account):
        self.account_list.remove(account)

    # generate unique account number for new user
    def generate_account_number(self):
        for i in range(100):
            account_number = str(random.randint(10000, 99999))
            if not self.check_account(account_number):
                return account_number  # return if the account number is unique
        return None
