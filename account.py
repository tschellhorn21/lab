class Account:

    def __init__(self, name, amount=0):
        self.account_name = name
        self.account_balance = amount

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self.account_balance += amount
            return True

    def withdraw(self, amount):
        if amount > self.account_balance or amount <= 0:
            return False
        else:
            self.account_balance -= amount
            return True

    def get_balance(self):
        return self.account_balance

    def get_name(self):
        return self.account_name
