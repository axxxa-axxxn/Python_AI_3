class Account:

    def __init__(self, account_number, name, balance=0):

        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount!")
            return

        self.balance += amount
        print("Deposit successful!")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount!")
            return

        if amount <= self.balance:

            self.balance -= amount
            print("Withdrawal successful!")

        else:

            print("Insufficient balance!")

    def display(self):

        print("\n----- Account Details -----")
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.balance)