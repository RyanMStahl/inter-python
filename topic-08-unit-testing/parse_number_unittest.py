import unittest

def parse(s):
    return 0.0

class ParseTests(unittest.TestCase):
    def test_parse_exists(self):
        "test that parse() can be called with a string and returns a float"
        n = parse("1")
        self.assertEqual(type(n),float)
    def test_parse_exists_again(self):
        "test that parse() can be called with a string and returns a float"
        n = parse("1")
        self.assertEqual(type(n),float)

if __name__ == "__main__":
    unittest.main()
    print("done.")