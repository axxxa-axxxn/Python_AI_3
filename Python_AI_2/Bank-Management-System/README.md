# 🏦 Bank Management System

A simple console-based Bank Management System built using Python and Object-Oriented Programming (OOP). This project allows users to create accounts, perform transactions, transfer funds between accounts, and manage account information through a menu-driven interface.

---

## 📋 Features

* Create new bank accounts
* Deposit money
* Withdraw money
* Check account balance
* Transfer money between accounts
* Display account details
* Duplicate account number validation
* Transaction amount validation
* Insufficient balance protection

---

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Classes and Objects
* Functions
* Lists and Data Structures
* Conditional Statements
* Loops

---

## 📁 Project Structure

```text
Bank-Management-System/

├── main.py
├── bank.py
├── account.py
├── README.md
└── requirements.txt
```

### File Description

* **main.py** → Application entry point and menu system
* **bank.py** → Banking operations and account management
* **account.py** → Account class and account-related methods
* **README.md** → Project documentation
* **requirements.txt** → Project dependencies

---

## 🚀 How to Run

### Clone the Repository

```bash
git clone https://github.com/your-ayelaahsan/Bank-Management-System.git
```

### Navigate to Project Directory

```bash
cd Bank-Management-System
```

### Run the Application

```bash
python main.py
```

---

## 💻 Menu Options

```text
=========================
    Banking System
=========================

1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Transfer Money
6. Exit
```

---

## 📌 Example Workflow

### Create Accounts

```text
Enter choice: 1
Enter account number: 101
Enter customer name: Ali

Account created successfully!
```

```text
Enter choice: 1
Enter account number: 102
Enter customer name: Ahmed

Account created successfully!
```

### Deposit Money

```text
Enter choice: 2
Enter account number: 101
Enter deposit amount: 5000

Deposit successful!
```

### Transfer Money

```text
Enter choice: 5

Enter sender account number: 101
Enter receiver account number: 102
Enter transfer amount: 2000

Transfer successful!

Ali New Balance: 3000
Ahmed New Balance: 2000
```

---

## ✅ Validation Features

The application handles:

* Invalid deposit amounts
* Invalid withdrawal amounts
* Duplicate account numbers
* Insufficient balance
* Invalid account numbers
* Self-transfer prevention

---

## 🎯 Learning Objectives

This project demonstrates:

* Object-Oriented Programming concepts
* Class design and interaction
* Modular programming
* Code organization
* Input validation
* Basic banking operations
* Git and GitHub workflow

---

## 👨‍💻 Author

AYELA AHSAN

---

## 📄 License

This project is developed for educational and learning purposes.