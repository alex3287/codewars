import unittest
from snail import snail


class MyTestCase(unittest.TestCase):

    def test_first(self):
        array = [[]]
        self.assertEqual(snail(array), [])

    def test_second(self):
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        self.assertEqual(snail(array), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_third(self):
        array = [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25]]
        self.assertEqual(snail(array), [1, 2, 3, 4, 5, 10, 15, 20, 25,
                                        24, 23, 22, 21, 16, 11, 6, 7,
                                        8, 9, 14, 19, 18, 17, 12, 13])


if __name__ == '__main__':
    unittest.main()
