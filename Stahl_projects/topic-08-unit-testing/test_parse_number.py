import unittest
from parse_number import parse

class Parse_tests(unittest.TestCase):
    def test_parse_returns_float(self):
        """
        test that parse() can be called with a string and returns a fload
        """
        n = 1
        m = parse("1")
        self.assertIsInstance(m, float)
        self.assertEqual(float(n), m)

    def test_parse_single_digit(self):
        digits = ['0', '1', '2', '3', '4', 
                  '5', '6', '7', '8', '9']
        #print("\n")
        for digit in digits:
            with self.subTest(digit):
                #print(f"Testing {digit}")
                self.assertIsInstance(parse(digit), float)
                self.assertEqual(float(digit), parse(digit))

    def test_parse_multiple_digits(self):
        self.assertEqual(parse('123'), 123)
        self.assertEqual(parse('123.456'), 123.456)

    def test_param_err(self):
        with self.assertRaisesRegex(ValueError, "input is not of type string"):
            parse(123)





if __name__ == "__main__":
    unittest.main()