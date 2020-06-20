import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(1, 5), 6)

    def test_multiply(self):
        self.assertEqual(katas.multiply(3, 3), 9)

    def test_power(self):
        self.assertEqual(katas.power(2, 3), 8)

    def test_factorial(self):
        self.assertEqual(katas.factorial(4), 24)

    def test_fibonacci(self):
        self.assertTrue(katas.fibonacci(8), 21)


if __name__ == '__main__':
    unittest.main()
