import unittest
from find_string import find_uniq

class MyTestClass(unittest.TestCase):
    def test_first(self):
        string = ['sdf','sfd','dfss','qwer']
        self.assertEqual(find_uniq(string),'qwer')

if __name__ == "__main__":
    unittest.main()