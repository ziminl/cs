import csv
import unittest
from ExtraCredit1 import *

class Testing(unittest.TestCase):
    def test_sort_fruits_alphabetically(self):
        fruits = ['apple', 'banana', 'orange', 'kiwi', 'strawberry', 'grape', 'mango', 'blueberry', 'pineapple', 'watermelon']
        self.assertListEqual(sorted(fruits), sort_fruits_alphabetically(fruits))

    def test_filter_fruits_by_length(self):
        fruits = ['apple', 'banana', 'orange', 'kiwi', 'strawberry', 'grape', 'mango', 'blueberry', 'pineapple', 'watermelon']
        filt_fruit = filter_fruits_by_length(fruits, 6)
        resp = ['banana', 'orange', 'strawberry', 'blueberry', 'pineapple', 'watermelon']
        self.assertListEqual(resp, filt_fruit)

    def test_searchBookTitle(self):
        books = [['a', 8.0, 1, True],
                 ['b', 16.0, 3, True],
                 ['b', 5.0, 2, True],
                 ['a', 2.0, 4, True],
                 ['a', 4.0, 5, True]]
        res = [['a', 8.0, 1, True],
                 ['a', 2.0, 4, True],
                 ['a', 4.0, 5, True]]
        self.assertListEqual(res, searchBookTitle(books, 'a'))

    def test_shakerSortBooks1(self):
        books = [['a', 8.0, 1, True],
                 ['b', 16.0, 3, True],
                 ['b', 5.0, 2, True],
                 ['a', 2.0, 4, True],
                 ['a', 4.0, 5, True]]
        asc_ord_price = [['a', 2.0, 4, True], ['a', 4.0, 5, True], ['b', 5.0, 2, True], ['a', 8.0, 1, True], ['b', 16.0, 3, True]]
        shakerSortBooks(books, "price", True)
        self.assertListEqual(asc_ord_price, books)

    def test_shakerSortBooks2(self):
        books = [['a', 8.0, 1, True],
                 ['b', 16.0, 3, True],
                 ['b', 5.0, 2, True],
                 ['a', 2.0, 4, True],
                 ['a', 4.0, 5, True]]
        asc_ord_quality = [['a', 8.0, 1, True], ['b', 5.0, 2, True], ['b', 16.0, 3, True], ['a', 2.0, 4, True], ['a', 4.0, 5, True]]
        shakerSortBooks(books, "quality", True)
        self.assertListEqual(asc_ord_quality, books)

    def test_shakerSortBooks3(self):
        books = [['a', 8.0, 1, True],
                 ['b', 16.0, 3, True],
                 ['b', 5.0, 2, True],
                 ['a', 2.0, 4, True],
                 ['a', 4.0, 5, True]]
        des_ord_price = [['b', 16.0, 3, True], ['a', 8.0, 1, True], ['b', 5.0, 2, True], ['a', 4.0, 5, True], ['a', 2.0, 4, True]]
        shakerSortBooks(books, "price", False)
        self.assertListEqual(des_ord_price, books)

    def test_shakerSortBooks4(self):
        books = [['a', 8.0, 1, True],
                 ['b', 16.0, 3, True],
                 ['b', 5.0, 2, True],
                 ['a', 2.0, 4, True],
                 ['a', 4.0, 5, True]]
        des_ord_quality = [['a', 4.0, 5, True], ['a', 2.0, 4, True], ['b', 16.0, 3, True], ['b', 5.0, 2, True], ['a', 8.0, 1, True]]
        shakerSortBooks(books, "quality", False)
        self.assertListEqual(des_ord_quality, books)

    def test_rangeQualityCheckBooks(self):
        books = [['a', 8.0, 1, True],
                 ['b', 16.0, 3, True],
                 ['b', 5.0, 2, True],
                 ['a', 2.0, 4, True],
                 ['a', 4.0, 5, True]]
        list_book = rangeQualityCheckBooks(books,[4,5])
        verif = True
        for book in list_book:
            if not(4<=book[2]<=5):
                verif = False
        self.assertEqual(True, verif)

    
if __name__ == '__main__':
    unittest.main()