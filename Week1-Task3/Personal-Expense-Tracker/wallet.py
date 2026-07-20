class Wallet:

    def __init__(self, balance):
        self.balance = balance


    def add_expense(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            return True

        return False


    def show_balance(self):
        return self.balance