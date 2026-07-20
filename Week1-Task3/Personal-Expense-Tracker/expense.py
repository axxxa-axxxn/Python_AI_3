class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category


    def display(self):
        print(
            f"Title: {self.title} | Amount: {self.amount} | Category: {self.category}"
        )