import unittest
from student_management import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("101", "Ayela", 20)

    def test_roll_number(self):
        self.assertEqual(self.student.roll_no, "101")

    def test_name(self):
        self.assertEqual(self.student.name, "Ayela")

    def test_age(self):
        self.assertEqual(self.student.age, 20)

    def test_str_method(self):
        expected = "Roll No: 101, Name: Ayela, Age: 20"
        self.assertEqual(str(self.student), expected)

    def test_repr_method(self):
        expected = "Student('101', 'Ayela', 20)"
        self.assertEqual(repr(self.student), expected)


if __name__ == "__main__":
    unittest.main()