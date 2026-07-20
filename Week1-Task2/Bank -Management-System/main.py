from bank import Bank



bank = Bank()



while True:


    print("""
=========================
 Simple Banking System
=========================

1. Create Account

2. Deposit Money

3. Withdraw Money

4. Check Balance

5. Exit

""")


    choice = input("Enter choice: ")



    if choice == "1":

        acc_no = int(input("Enter account number: "))

        name = input("Enter customer name: ")


        bank.create_account(acc_no, name)



    elif choice == "2":

        acc_no = int(input("Enter account number: "))


        account = bank.find_account(acc_no)


        if account:


            amount = float(input("Enter deposit amount: "))

            account.deposit(amount)


        else:

            print("Account not found!")



    elif choice == "3":

        acc_no = int(input("Enter account number: "))


        account = bank.find_account(acc_no)


        if account:


            amount = float(input("Enter withdrawal amount: "))

            account.withdraw(amount)


        else:

            print("Account not found!")



    elif choice == "4":

        acc_no = int(input("Enter account number: "))


        account = bank.find_account(acc_no)


        if account:

            account.display()


        else:

            print("Account not found!")



    elif choice == "5":

        print("Thank you for using banking system")

        break



    else:

        print("Invalid choice!")