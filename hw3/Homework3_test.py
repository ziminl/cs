import csv
import unittest
from Homework3 import *

class Testing(unittest.TestCase):
    def test_checkValidInterval(self):
        query = 10
        lst = [5, 30, 178, 45]
        self.assertEqual(True, checkValidInterval(lst, query))
        self.assertEqual(False, checkValidInterval(lst, -5))

    def test_backwardLinearSearch(self):
        query = 10
        lst = [5, 30, 178, 45, 44, 25, 100, 90]
        res1 = backwardLinearSearch(lst, 5, 7, 5)
        res2 = backwardLinearSearch(lst, 178, 4, 0)
        res3 = backwardLinearSearch(lst, 25, 6, 1)
        self.assertEqual(None, res1)
        self.assertEqual(2, res2)
        self.assertEqual(5, res3)
    
    def test_findStepSize(self):
        lst = [1,2,3,4]
        self.assertEqual(int(4**0.5), findStepSize(lst))

    def test_jumpSearch1(self):
        lst = [5, 18, 34, 56, 78, 88, 98, 100, 500, 1000, 2000, 2200]
        ind1 = jumpSearch(lst, 18) #--> 1
        self.assertEqual(1, ind1)

    def test_jumpSearch2(self):
        lst = [5, 18, 34, 56, 78, 88, 98, 100, 500, 1000, 2000, 2200]
        ind2 = jumpSearch(lst, 2000) # --> 10
        self.assertEqual(10, ind2)

    def test_jumpSearch3(self):
        lst = [5, 18, 34, 56, 78, 88, 98, 100, 500, 1000, 2000, 2200]
        ind3 = jumpSearch(lst, 4) # --> None
        self.assertEqual(None, ind3)

    def test_jumpSearch4(self):
        lst = [5, 18, 34, 56, 78, 88, 98, 100, 500, 1000, 2000, 2200]
        ind4 = jumpSearch(lst, 79) # --> None
        self.assertEqual(None, ind4)

    
if __name__ == '__main__':
    unittest.main()