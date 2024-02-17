
import unittest
from main import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    # Test empty string
    def test_empty_string(self):
        self.assertEqual(self.calc.add_str(""), 0)

if __name__ == '__main__':
    unittest.main()