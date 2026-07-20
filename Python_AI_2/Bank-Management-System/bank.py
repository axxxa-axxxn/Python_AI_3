from account import Account


class Bank:

    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, name):

        existing_account = self.find_account(account_number)

        if existing_account:
            print("Account number already exists!")
            return

        account = Account(account_number, name)
        self.accounts.append(account)

        print("Account created successfully!")

    def find_account(self, account_number):

        for account in self.accounts:

            if account.account_number == account_number:
                return account

        return None

    def transfer_money(self, sender_acc, receiver_acc, amount):

        sender = self.find_account(sender_acc)
        receiver = self.find_account(receiver_acc)

        if sender is None:
            print("Sender account not found!")
            return

        if receiver is None:
            print("Receiver account not found!")
            return

        if sender_acc == receiver_acc:
            print("Cannot transfer to the same account!")
            return

        if amount <= 0:
            print("Invalid amount!")
            return

        if sender.balance < amount:
            print("Insufficient balance!")
            return

        sender.balance -= amount
        receiver.balance += amount

        print("Transfer successful!")

        print(f"{sender.name} New Balance: {sender.balance}")
        print(f"{receiver.name} New Balance: {receiver.balance}")

    def show_all_accounts(self):

        if not self.accounts:
            print("No accounts found!")
            return

        for account in self.accounts:
            account.display()