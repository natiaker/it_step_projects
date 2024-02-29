class Account:
    def __init__(self, account_number, name, balance, pin):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.pin = pin

    def change_pin(self):
        new_pin = int(input("Enter the new pin (4 digits): "))
        if new_pin == self.pin:
            return "You are currently using this PIN"
        else:
            self.pin = new_pin
            return "PIN changed successfully"


account1 = Account("01", "John", 1000, "1234")
print(account1.pin)
account1.change_pin()
print(account1.pin)