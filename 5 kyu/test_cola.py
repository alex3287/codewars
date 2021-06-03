import unittest
from duoble import whoIsNext


class MyTest(unittest.TestCase):

    def test_first(self):
        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
        self.assertEquals(whoIsNext(names, 2), "Leonard")

    def test_second(self):
        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
        self.assertEquals(whoIsNext(names, 5), "Howard")
        self.assertEquals(whoIsNext(names, 4), "Rajesh")

    def test_third(self):
        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
        self.assertEquals(whoIsNext(names, 12), "Rajesh")
        self.assertEquals(whoIsNext(names, 13), "Rajesh")

    def test_fourth(self):
        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
        self.assertEquals(whoIsNext(names, 52), "Penny")
        self.assertEquals(whoIsNext(names, 53), "Penny")
        self.assertEquals(whoIsNext(names, 54), "Penny")
        self.assertEquals(whoIsNext(names, 55), "Penny")
        self.assertEquals(whoIsNext(names, 56), "Penny")
        self.assertEquals(whoIsNext(names, 57), "Penny")
        self.assertEquals(whoIsNext(names, 58), "Penny")
        self.assertEquals(whoIsNext(names, 59), "Penny")

    def test_fifth(self):
        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]    
        self.assertEquals(whoIsNext(names, 188), "Leonard")
        self.assertEquals(whoIsNext(names, 219), "Leonard")

    def test_sixth(self):
        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]    
        self.assertEquals(whoIsNext(names, 770), "Leonard")
        self.assertEquals(whoIsNext(names, 3200), "Leonard")
    
    def test_seventh(self):
        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]    
        self.assertEquals(whoIsNext(names, 7230702951), "Leonard")
        

if __name__ == "__main__":
    unittest.main()
