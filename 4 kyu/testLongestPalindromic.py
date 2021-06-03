import unittest
from longestPalindromic import longest_palindrome

class MyTestCase(unittest.TestCase):
    def test_first(self):
        test = longest_palindrome('')
        self.assertEqual(test, '')

    def test_second(self):
        test = longest_palindrome('madam')
        self.assertEqual(test, 'madam')

    def test_third(self):
        test = longest_palindrome('babad')
        self.assertEqual(test, 'bab')

    def test_fourth(self):
        test = longest_palindrome('cbbd')
        self.assertEqual(test, 'bb')

    def test_fifth(self):
        test = longest_palindrome('ttaaftffftfaafatf')
        self.assertEqual(test, 'aaftffftfaa')

    def test_sixth(self):
        test = longest_palindrome('ababbab')
        self.assertEqual(test, 'babbab')

    def test_seventh(self):
        test = longest_palindrome('dde')
        self.assertEqual(test, 'dd')

    def test_eight(self):
        test = longest_palindrome('abv')
        self.assertEqual(test, 'a')

if __name__ == '__main__':
    unittest.main()
