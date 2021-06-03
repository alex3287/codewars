import unittest
from next_smoler import next_smaller


class MyTestCase(unittest.TestCase):
    def test_first(self):
        result = next_smaller(20099)
        self.assertEqual(result, -1)
        self.assertEqual(next_smaller(222), -1)
        self.assertEqual(next_smaller(99), -1)
        self.assertEqual(next_smaller(555555), -1)

    def test_second(self):
        result = next_smaller(12345)
        self.assertEqual(result, -1)

    def test_third(self):
        result = next_smaller(1000)
        self.assertEqual(result, -1)

    def test_fourth(self):
        result = next_smaller(35555)
        self.assertEqual(result, -1)

    def test_fifth(self):
        result = next_smaller(135)
        self.assertEqual(result, -1)

    def test_sixth(self):
        result = next_smaller(1234567908)
        self.assertEqual(result, 1234567890)

    def test_seventh(self):
        result = next_smaller(907)
        self.assertEqual(result, 790)

    def test_eighth(self):
        result = next_smaller(451)
        self.assertEqual(result, 415)

    def test_ninth(self):
        result = next_smaller(414)
        self.assertEqual(result, 144)

    def test_tenth(self):
        result = next_smaller(29009)
        self.assertEqual(result, 20990)

    def test_elevnth(self):
        result = next_smaller(1207)
        self.assertEqual(result, 1072)

    def test_twelvth(self):
        result = next_smaller(1414)
        self.assertEqual(result, 1144)

    def test_threteenth(self):
        result = next_smaller(2759)
        self.assertEqual(result, 2597)

    def test_fourteenth(self):
        self.assertEqual(next_smaller(513), 351)

    def test_fifteenth(self):
        self.assertEqual(next_smaller(52682568), 52668852)
        self.assertEqual(next_smaller(2219712279), 2219297721)
        


if __name__ == '__main__':
    unittest.main()