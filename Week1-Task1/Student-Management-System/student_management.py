class Student:
    """
    Represents a student with roll number, name, and age.
    """

    def __init__(self, roll_no, name, age):
        self.__roll_no = roll_no
        self.__name = name
        self.__age = age

    @property
    def roll_no(self):
        return self.__roll_no

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return (
            f"Roll No: {self.__roll_no}, "
            f"Name: {self.__name}, "
            f"Age: {self.__age}"
        )

    def __repr__(self):
        return (
            f"Student('{self.__roll_no}', "
            f"'{self.__name}', {self.__age})"
        )


class StudentManagementSystem:
    """
    Manages student records using a list of Student objects.
    """

    def __init__(self):
        self.students = []

    def add_student(self):
        """
        Add a new student to the system.
        """
        roll_no = input("Enter Roll Number: ").strip()

        if not roll_no:
            print("Roll Number cannot be empty.")
            return

        # Prevent duplicate roll numbers
        for student in self.students:
            if student.roll_no == roll_no:
                print("Roll Number already exists.")
                return

        name = input("Enter Name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                return

        except ValueError:
            print("Age must be a number.")
            return

        student = Student(roll_no, name, age)
        self.students.append(student)

        print("Student added successfully!")

    def delete_student(self):
        """
        Delete a student using roll number.
        """
        roll_no = input("Enter Roll Number to delete: ").strip()

        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found.")

    def show_students(self):
        """
        Display all students sorted by roll number.
        """
        if not self.students:
            print("No students available.")
            return

        print("\n===== Student List =====")

        for student in sorted(self.students, key=lambda s: s.roll_no):
            print(student)

        print(f"\nTotal Students: {len(self.students)}")

    def search_student(self):
        """
        Search for a student by roll number.
        """
        roll_no = input("Enter Roll Number to search: ").strip()

        for student in self.students:
            if student.roll_no == roll_no:
                print("\nStudent Found:")
                print(student)
                return

        print("Student not found.")

    def menu(self):
        """
        Display the main menu and handle user choices.
        """
        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. Delete Student")
            print("3. Show Students")
            print("4. Search Student")
            print("5. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.delete_student()
            elif choice == "3":
                self.show_students()
            elif choice == "4":
                self.search_student()
            elif choice == "5":
                print("Program Ended.")
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    """
    Program entry point.
    """
    sms = StudentManagementSystem()
    sms.menu()


if __name__ == "__main__":
    main()