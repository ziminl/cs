import unittest
from Homework4 import *
import math

def distComput(lst,q):
    lst_dist = []
    for i in range(len(lst)):
        lst_dist.append(abs(lst[i]-q))
    return lst_dist

def findMin(lst):
    min = lst[0]
    for i in range(1,len(lst)):
        if lst[i]<min:
            min = lst[i]
    return min

def countOccurence(lst, query):
    count = 0
    for value in lst:
        if value == query:
            count += 1
    return count

class Testing(unittest.TestCase):
    def test_wallisPi(self):
        pi = math.pi
        self.assertEqual(True, (pi-0.1) < wallisPi(900)*2 < (pi+0.1))

    def test_gregoryPi(self):
        pi = math.pi
        self.assertEqual(True, (pi-0.1) < gregoryPi(900)*4 < (pi+0.1))

    def test_ramanujanPi(self):
        pi = math.pi
        self.assertEqual(True, (pi-0.1) < (9801/(2*(2**0.5)*ramanujanPi(100))) < (pi+0.1))

    def test_distComputRec(self):
        query = 10
        lst = [5, 30, 178, 45, 44, 25, 100, 90]
        lst_dist_rec = []
        distComputRec(lst, query, lst_dist_rec)
        self.assertListEqual(distComput(lst,query), lst_dist_rec)
    
    def test_findMinRec(self):
        lst = [1,2,3,4, 0 , 100, 200]
        self.assertEqual(findMin(lst), findMinRec(lst))

    def test_countOccurenceRec(self):
        query = 56
        lst = [5, 18, 34, 56, 78, 88, 98, 100, 500, 56, 1000, 2000, 56, 2200]
        self.assertEqual(countOccurence(lst, query), countOccurenceRec(lst, query))

    def test_checkSortRec(self):
        lst1 = [5, 18, 34, 56, 78, 88, 98, 100, 500, 1000, 2000, 2200]
        self.assertEqual(checkSortRec(lst1), True)
        lst2 = [5, 18, 34, 56, 78, 100, 88, 98, 100, 500, 1000, 2000, 2200]
        self.assertEqual(checkSortRec(lst2), False)

    
if __name__ == '__main__':
    unittest.main()