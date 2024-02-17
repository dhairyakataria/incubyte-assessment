
import unittest
from main import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    # Test empty string
    def test_empty_string(self):
        self.assertEqual(self.calc.add_str(""), 0)

    # Test single number
    def test_single_number(self):
        self.assertEqual(self.calc.add_str("1"), 1)

    # Test multiple numbers separated by commas
    def test_multiple_numbers_commas(self):
        self.assertEqual(self.calc.add_str("1,5"), 6)

    def test_multiple_numbers_commas_2(self):
        self.assertEqual(self.calc.add_str("1, 5 ,  "), 6)

if __name__ == '__main__':
    unittest.main()