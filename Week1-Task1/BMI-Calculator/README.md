# Python Internship Projects

Welcome to the collection of Python projects developed during my internship. This repository houses standalone applications showcasing Object-Oriented Programming (OOP), input validation, unit testing, and GUI development in Python.

---

## Repository Structure

```text
Python_AI-/
│
├── BMI-Calculator/           # Graphical & CLI BMI calculation project
│   ├── BMI_Calculator.py     # Core CLI implementation
│   ├── test_BMI_Calculator.py# Unit tests for calculations
│   └── requirements.txt      # Dependencies
│
└── Student-Management-System/ # OOP-based student tracking project
    ├── student_management.py # Main OOP implementation
    ├── test_student_management.py # Unit tests for students log
    └── requirements.txt      # Dependencies
```

---

## Projects Included

### 1. [BMI Calculator](./BMI-Calculator/)
A command-line based (and expandable GUI-based) Body Mass Index calculator.
- **Key Features**: 
  - Weight categorization (Underweight, Normal, Overweight, Obese).
  - Validation for inputs greater than zero.
  - Comprehensive unit testing.
- **Run the CLI app**:
  ```bash
  cd BMI-Calculator
  python BMI_Calculator.py
  ```

### 2. [Student Management System](./Student-Management-System/)
An Object-Oriented Programming (OOP) console application to manage student logs.
- **Key Features**:
  - Add, search, delete, and list students.
  - Custom properties and private attributes (Encapsulation).
  - Input validation for Roll Numbers, Names, and Ages.
- **Run the app**:
  ```bash
  cd Student-Management-System
  python student_management.py
  ```

---

## Running All Unit Tests

Each project includes unit tests. To run tests:

**For BMI Calculator**:
```bash
cd BMI-Calculator
python -m unittest test_BMI_Calculator.py
```

**For Student Management System**:
```bash
cd Student-Management-System
python -m unittest test_student_management.py
```

---

## Author
**Ayela Ahsan**
- GitHub: [ayela-ahsan](https://github.com/ayela-ahsan)
- Email: ayelaahsan@gmail.com
