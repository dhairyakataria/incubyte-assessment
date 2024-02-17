
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

    # Test invalid input
    def test_invalid_input_trailing_comma_newline(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add_str("1,\n")
        self.assertEqual(str(context.exception), "Invalid input format: trailing comma followed by newline")

    # Test multiple numbers separated by newlines
    def test_multiple_numbers_newlines(self):
        self.assertEqual(self.calc.add_str("1\n2,3"), 6)

    # Test custom delimiter
    def test_custom_delimiter(self):
            self.assertEqual(self.calc.add_str("//;\n4;5;7"), 16)

    

if __name__ == '__main__':
    unittest.main()