### ZERO MATRIX ###

import unittest
from typing import List

def zero_matrix(A: List[List[int]]) -> List[List[int]]:
    rows_tracker = set()
    cols_tracker = set()
    rows = len(A)
    cols = len(A[0])

    for row in range(rows):
        for col in range(cols):
            if not A[row][col]:
                rows_tracker.add(row)
                cols_tracker.add(col)

    for row in rows_tracker:
        for col in range(cols):
            A[row][col] = 0
    
    for col in cols_tracker:
        for row in range(rows):
            A[row][col] = 0
    
    return A



if __name__ == "__main__":
    print(zero_matrix([[1,0,3], [10,4,5], [7,8,9]]))

