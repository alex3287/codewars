import unittest
from interleaving_Arrays import interleave

class MyTestCase(unittest.TestCase):
    # def test_first(self):
    #     result = interleave([])
    #     self.assertEqual(result, [])

    def test_second(self):
        result = interleave([1, 2, 3], ["c", "d", "e"])
        self.assertEqual(result, [1, "c", 2, "d", 3, "e"])

    def test_third(self):
        result = interleave([1, 2, 3], ["c", "d", "e"], [4, 5, 6])
        self.assertEqual(result, [1, "c", 4, 2, "d", 5, 3, "e", 6])


if __name__ == '__main__':
    unittest.main()
