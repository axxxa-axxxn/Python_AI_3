import unittest

from models.patient import Patient


class TestPatient(unittest.TestCase):

    def test_patient_creation(self):

        patient = Patient(
            "P001",
            "Sara",
            25,
            "Female",
            "1234567890",
            "sara@gmail.com",
            "A+"
        )

        self.assertEqual(
            patient.blood_group,
            "A+"
        )


if __name__ == "__main__":
    unittest.main()