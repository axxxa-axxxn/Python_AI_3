import unittest

from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment


class TestAppointment(unittest.TestCase):

    def test_appointment_creation(self):

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

        patient = Patient(
            "P001",
            "Sara",
            25,
            "Female",
            "1234567890",
            "sara@gmail.com",
            "A+"
        )

        appointment = Appointment(
            "A001",
            doctor,
            patient,
            "2026-07-20",
            "10:00 AM"
        )

        self.assertEqual(
            appointment.status,
            "Scheduled"
        )


if __name__ == "__main__":
    unittest.main()