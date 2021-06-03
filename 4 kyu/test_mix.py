import unittest
from mix import mix

class MyTestClass(unittest.TestCase):
    def test_first(self):
        a, b = "Are they here", "yes, they are here"
        self.assertEqual(mix(a, b), "2:eeeee/2:yy/=:hh/=:rr")

    def test_second(self):
        a, b = "looping is fun but dangerous", "less dangerous than coding"
        self.assertEqual(mix(a, b), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")

    def test_third(self):
        a, b = " In many languages", " there's a pair of functions"
        self.assertEqual(mix(a, b), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")

if __name__ == '__main__':
    unittest.main()
