import unittest

from date import *

class MyTestClass(unittest.TestCase):
    def test_first(self):
        self.assertEqual(format_duration(5),'5 seconds')

    def test_second(self):
        self.assertEqual(format_duration(0),'now')

    def test_third(self):
        self.assertEqual(format_duration(3600), '1 hour')

    def test_fours(self):
        self.assertEqual(format_duration(3661), '1 hour, 1 minute and 1 second')

    def test_fours(self):
        self.assertEqual(format_duration(157795260), '5 years, 1 day, 8 hours and 1 minute')

if __name__ == '__main__':
    unittest.main()