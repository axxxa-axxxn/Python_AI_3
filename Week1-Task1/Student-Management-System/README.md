# Student Management System

A simple console-based Student Management System built using Python and Object-Oriented Programming (OOP). The application allows users to add, search, delete, and display student records while demonstrating core Python and OOP concepts.

---

## Features

- Add Student
- Delete Student
- Search Student
- Show All Students
- Prevent Duplicate Roll Numbers
- Input Validation
- Exception Handling
- Display Total Number of Students
- Display Students Sorted by Roll Number
- Encapsulation using Private Attributes
- Magic Methods (`__init__`, `__str__`, `__repr__`)

---

## Technologies Used

- Python 3
- Python Standard Library (`unittest`)

---

## Concepts Covered

- Classes
- Objects
- Methods
- Lists
- Encapsulation
- Properties (`@property`)
- Exception Handling
- Magic Methods
- Docstrings
- Unit Testing

---

## Project Structure

```text
Student-Management-System/
│
├── student_management.py
├── test_student_management.py
├── README.md
├── requirements.txt
└── .gitignore
```

> **Note:** The `__pycache__` folder is generated automatically by Python and is ignored using `.gitignore`, so it is not included in the repository.

---

## Requirements

- Python 3.8 or higher

---

## Running the Project

```bash
python student_management.py
```

---

## Running Unit Tests

```bash
python -m unittest test_student_management.py
```

or

```bash
python test_student_management.py
```

---

## Example Output

### Add Student

```text
Enter Roll Number: 101
Enter Name: Ali
Enter Age: 20

Student added successfully!
```

### Show Students

```text
===== Student List =====
Roll No: 101, Name: Ali, Age: 20

Total Students: 1
```

---

## Learning Outcomes

This project demonstrates:

- Object-Oriented Programming (OOP)
- Encapsulation
- Python Magic Methods
- Input Validation
- Exception Handling
- Unit Testing using `unittest`

---

## Author

**Ayela Ahsan**

---

If you found this project useful, consider giving it a star on GitHub.