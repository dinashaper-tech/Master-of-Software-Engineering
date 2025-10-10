import unittest
from week11_1 import Shape, Rectangle, Square, multiply

class TestMultiply(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_with_zero(self):
        self.assertEqual(multiply(0, 5), 0)



if __name__ == "__main__":
    
    unittest.main(argv=[''], exit=False)
