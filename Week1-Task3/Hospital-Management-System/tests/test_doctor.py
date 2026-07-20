import unittest

from models.doctor import Doctor


class TestDoctor(unittest.TestCase):

    def test_doctor_creation(self):

        doctor = Doctor(
            "D001",
            "Ali",
            35,
            "Male",
            "1234567890",
            "ali@gmail.com",
            "Cardiology",
            10
        )

        self.assertEqual(
            doctor.specialization,
            "Cardiology"
        )


if __name__ == "__main__":
    unittest.main()