import unittest
from alphabetic import listPosition

class MyTestClass(unittest.TestCase):
    def test_one(self):
        self.assertEqual(listPosition('AAAB'), 1)
    def test_two(self):
        self.assertEqual(listPosition('BAAA'), 4)
    def test_three(self):
        self.assertEqual(listPosition('ABAB'), 2)
    def test_four(self):
        self.assertEqual(listPosition('S'), 1)
    def test_five(self):
        self.assertEqual(listPosition('QUESTION'), 24572)
    def test_six(self):
        self.assertEqual(listPosition('S'), 1)

if __name__ == '__main__':
    unittest.main()

