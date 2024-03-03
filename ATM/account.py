import json

ACCOUNT_FILE = "accounts.json"


class Account:
    def __init__(self, account_number, name, balance, pin):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.pin = pin

    def __str__(self):
        return (f"Account number: {self.account_number}, Name: {self.name}, Balance: {self.balance}, "
                f"PIN: {self.pin}")

    def getbalance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
        elif self.balance < amount:
            print("Not enough money")
        else:
            self.balance -= amount

    def change_pin(self, pin):
        self.pin = pin

    def get_pin(self):
        return self.pin


def serialization_func(obj):
    if isinstance(obj, Account):
        return {"account_number": obj.account_number, "name": obj.name, "balance": obj.balance, "pin": obj.pin}
    raise TypeError(f'Not type of Account')


def deserialization_func(obj):
    return Account(obj["account_number"], obj["name"], obj["balance"], obj["pin"])


class AccountManager:
    def __init__(self):
        self.account_list = []

    def write_accounts(self):
        with open(ACCOUNT_FILE, 'w') as json_file:
            json.dump(self.account_list, json_file, default=serialization_func, indent=4)

    def read_accounts(self):
        with open(ACCOUNT_FILE, 'r') as json_file:
            new_account_list = json.load(json_file, object_hook=deserialization_func)
        self.account_list = new_account_list

    def add_account(self, account):
        self.account_list.append(account)

    def check_account(self, account_number):
        for account in self.account_list:
            if account.get_account_number() == account_number:
                return account
        return None

    def delete_account(self, account):
        self.account_list.remove(account)
