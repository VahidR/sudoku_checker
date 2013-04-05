import unittest 
#from soduku.soduku import *
from soduku import *



correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]


incorrect6 = [[0,1,2], 
              [2,0,1], 
              [1,2,0]]

class SodukuTest(unittest.TestCase):
    
    def test_if_soduku_works_correct(self):
        self.assertEqual(check_sudoku(correct), True)
 
    def test_if_soduku_works_incorrect(self):
        self.assertEqual(check_sudoku(incorrect), False)

    def test_if_soduku_works_incorrect2(self):
        self.assertEqual(check_sudoku(incorrect2), False)

    def test_if_soduku_works_incorrect3(self):
        self.assertEqual(check_sudoku(incorrect3), False)

    def test_if_soduku_works_incorrect4(self):
        self.assertEqual(check_sudoku(incorrect4), False)

    def test_if_soduku_works_incorrect5(self):
        self.assertEqual(check_sudoku(incorrect5), False)

    def test_if_soduku_works_incorrect6(self):
        self.assertEqual(check_sudoku(incorrect6), False)




if __name__ == '__main__':
    unittest.main()

