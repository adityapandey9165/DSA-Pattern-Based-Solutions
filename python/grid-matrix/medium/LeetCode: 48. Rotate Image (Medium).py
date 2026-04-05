"""
LeetCode: 48. Rotate Image (Medium)
Problem Link: https://leetcode.com/problems/rotate-image/
Author: Aditya Pandey
Date: 2026-04-05

------------------------------------------------------------
Problem:
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees clockwise in-place.

You must modify the input matrix directly and not return a new one.

------------------------------------------------------------
Pattern:
Matrix Manipulation / In-place Transformation

------------------------------------------------------------
Approach:
A 90-degree clockwise rotation can be done in two steps:

1. Transpose the matrix
   - Swap matrix[r][c] with matrix[c][r] for all r < c
   - This flips rows and columns(means Transpose the matrix so the rows become cols and cols become rows

2. Reverse each row
   - After transpose, reverse every row
   - This gives the final clockwise rotation

------------------------------------------------------------
Why this works:
Original matrix:
    1 2 3
    4 5 6
    7 8 9

After transpose:
    1 4 7
    2 5 8
    3 6 9

After reversing each row:
    7 4 1
    8 5 2
    9 6 3

That is exactly the 90-degree clockwise rotated matrix.

------------------------------------------------------------
Time Complexity:
O(n^2)

Space Complexity:
O(1)

------------------------------------------------------------
Things to Pay Attention To:
- Only process the upper triangle while transposing
- Reverse each row after transposing
- This is an in-place operation
- Do not create a separate matrix unless asked
- The matrix is square (n x n)
------------------------------------------------------------
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose
        for r in range(n):
            for c in range(r + 1, n):  # started loop from r_1 to avais doble swapping that will reset the changes we have done like 0,1)->(1,0) then (1,0)->(0,1) 
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Step 2: Reverse each row
        for r in range(n):
            l, rt = 0, n - 1
            while l < rt:
                matrix[r][l], matrix[r][rt] = matrix[r][rt], matrix[r][l]
                l += 1
                rt -= 1


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sol.rotate(matrix1)
    print(matrix1)
    # Expected:
    # [[7,4,1],[8,5,2],[9,6,3]]

    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    sol.rotate(matrix2)
    print(matrix2)
    # Expected:
    # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
