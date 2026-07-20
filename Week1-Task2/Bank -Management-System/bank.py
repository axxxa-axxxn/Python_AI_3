from account import Account



class Bank:


    def __init__(self):

        self.accounts = []



    def create_account(self, account_number, name):

        account = Account(account_number, name)

        self.accounts.append(account)

        print("Account created successfully!")



    def find_account(self, account_number):

        for account in self.accounts:

            if account.account_number == account_number:

                return account


        return None