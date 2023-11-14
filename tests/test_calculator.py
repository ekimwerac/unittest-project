# tests/test_calculator.py
import unittest
from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Optional: Set up resources before each test
        pass

    def tearDown(self):
        # Optional: Clean up resources after each test
        pass

    def test_add(self):
        calculator = Calculator()
        result = calculator.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(2, 7)
        self.assertEqual(result, 14)

    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(8, 2)
        self.assertEqual(result, 4)

        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()

