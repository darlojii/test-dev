from main import home, reverse_string
import unittest

class TestMain(unittest.TestCase):
    def test_home(self):
        self.assertEquals('Hello, World!', home())

    def test_reverse_string(self):
        self.assertEquals('eMesreveR', reverse_string('ReverseMe'))

if __name__ == '__main__':
    unittest.main()