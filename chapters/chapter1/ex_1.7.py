### ROTATE A ###

import unittest
from typing import List

def rotate_A(A: List[List[int]]) -> List[List[int]]:
    #check if format is valid
    if (len(A) == 0 or len(A) != len(A[0])):
        return False

    last = len(A)
    for row in range(len(A)//2):
        for col in range(row, last-row-1):
            temp = A[row][col]
            A[row][col] = A[last-1-col][row]
            A[last-1-col][row] = A[last-1-row][last-1-col]
            A[last-1-row][last-1-col] = A[col][last-1-row]
            A[col][last-1-row] = temp           

    return A

class TestRotation(unittest.TestCase):

    def test_3x3(self):
        self.assertEqual([[7,4,1], [8,5,2], [9,6,3]], rotate_A([[1,2,3], [4,5,6], [7,8,9]]))
    
    def test_1x1(self):
        self.assertEqual([[1]], rotate_A([[1]]))
    
    def test_2x2(self):
        self.assertEqual([[3,1], [4,2]], rotate_A([[1,2], [3,4]]))


if __name__ == "__main__":
    unittest.main()