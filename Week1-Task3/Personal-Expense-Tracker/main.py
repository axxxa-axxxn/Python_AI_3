from expense import Expense
from wallet import Wallet


expenses = []


# Get wallet amount safely
while True:
    try:
        amount = float(input("Enter your initial wallet amount: "))

        if amount < 0:
            print("Wallet amount cannot be negative")
            continue

        break

    except ValueError:
        print("Invalid input! Please enter a number.")


wallet = Wallet(amount)



while True:

    print("\n===== Personal Expense Tracker =====")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Balance")
    print("4. Exit")


    choice = input("Enter choice: ")


    if choice == "1":

        title = input("Enter expense name: ")

        # Validate expense amount
        while True:
            try:
                expense_amount = float(input("Enter amount: "))

                if expense_amount <= 0:
                    print("Amount must be greater than zero")
                    continue

                break

            except ValueError:
                print("Invalid amount! Please enter numbers only.")


        category = input("Enter category: ")


        if wallet.add_expense(expense_amount):

            expense = Expense(
                title,
                expense_amount,
                category
            )

            expenses.append(expense)

            print("Expense Added Successfully")

        else:
            print("Not enough balance")



    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses found")

        else:

            print("\n----- Expenses -----")

            for expense in expenses:
                expense.display()



    elif choice == "3":

        print(
            "Remaining Balance:",
            wallet.show_balance()
        )



    elif choice == "4":

        print("Thank you for using Expense Tracker!")
        break


    else:
        print("Invalid choice! Please select 1-4.")