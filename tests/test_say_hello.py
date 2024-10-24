import unittest
from python_example import say_hello

class TestSayHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
