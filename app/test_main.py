from main import home, reverse_string
import unittest

class TestMain(unittest.TestCase):
    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'Hello, World!')

    def test_reverse_string(self):
        response = self.app.get('/ReverseMe')
        self.assertEqual(response.data, b'eMesreveR')

if __name__ == '__main__':
    unittest.main()