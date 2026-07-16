import unittest
from BMI_Calculator import calculate_bmi

class TestBMICalculator(unittest.TestCase):

    def test_normal_bmi(self):
        self.assertAlmostEqual(calculate_bmi(60, 1.65), 22.04, places=2)

    def test_underweight_bmi(self):
        self.assertAlmostEqual(calculate_bmi(45, 1.70), 15.57, places=2)

if __name__ == "__main__":
    unittest.main()