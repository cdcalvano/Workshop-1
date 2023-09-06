import unittest
import source 


class TestSubtraction(unittest.TestCase):
    def testSub1(self): 
        self.assertEqual(4, source.performSub(5, 1), "Bug in code!")

    def testSub2(self):
        self.assertEqual(1, source.performSub(2, 1), "Bug in code!")
    
    def testSub3(self):
        self.assertEqual(-1, source.performSub(2, 3), "Bug in code!")

class TestAddition(unittest.TestCase):
    def testAdd1(self): 
        self.assertEqual(3, source.performAdd(2, 1), "Bug in code!")

    def testAdd2(self): 
        self.assertEqual(0, source.performAdd(1, -1), "Bug in code!")

class TestMultiplication(unittest.TestCase):
    def testMult1(self):
        self.assertEqual(6, source.performMult(2, 3), "Bug in code!")

    def testMult2(self):
        self.assertEqual(-3, source.performMult(-1, 3), "Bug in code!")

class TestDivision(unittest.TestCase):
    def testDiv1(self):
        self.assertEqual(2, source.performDiv(6, 3), "Bug in code!")

    def testDiv2(self):
        self.assertEqual(-1, source.performDiv(-2, 2), "Bug in code!")



class TestDivision(unittest.TestCase):


if __name__ == '__main__': 
    unittest.main() 