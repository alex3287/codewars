import unittest
from Write_out_numbers import number2words


class MyTestClass(unittest.TestCase):
    def test_zero(self):
        number = 0
        self.assertEqual(number2words(number), 'zero')

    def test_first(self):
        number = 11
        self.assertEqual(number2words(number), 'eleven')

    def test_second(self):
        number = 40
        self.assertEqual(number2words(number), 'forty')

    def test_fourth(self):
        number = 22
        self.assertEqual(number2words(number), 'twenty-two')

    def test_fifth(self):
        number = 87
        self.assertEqual(number2words(number), 'eighty-seven')

    def test_sixth(self):
        number = 457
        self.assertEqual(number2words(number), 'four hundred fifty-seven')


if __name__ == '__main__':
    unittest.main()