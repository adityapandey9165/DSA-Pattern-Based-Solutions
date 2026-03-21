"""
LeetCode: 3643. Flip Square Submatrix Vertically (Easy)
Problem Link: https://leetcode.com/problems/flip-square-submatrix-vertically/
Author: Aditya Pandey
Date: 2026-03-21

Problem:
You are given a 2D integer grid and three integers x, y, and k.

The parameters define a k x k square submatrix whose top-left corner is at
(grid row = x, grid col = y).

Your task is to flip that square submatrix vertically, which means:
- the first row of the submatrix becomes the last row
- the second row becomes the second last row
- and so on

All cells outside the selected submatrix must remain unchanged.

------------------------------------------------------------
Pattern:
Matrix Simulation / In-place row swapping

------------------------------------------------------------
Approach:
To flip a square submatrix vertically, we only need to swap row pairs
inside that submatrix.

For a k x k submatrix:
- row x swaps with row x + k - 1
- row x + 1 swaps with row x + k - 2
- and so on

We only need to process the first half of the rows:
- that is, k // 2 rows

For each pair of rows, swap all k elements from column y to y + k - 1.

------------------------------------------------------------
Why this works:
A vertical flip means reversing row order, not reversing values inside each row.
So the submatrix is transformed by swapping whole rows within the selected square.

------------------------------------------------------------
Time Complexity:
O(k^2)

Space Complexity:
O(1)

------------------------------------------------------------
Things to Pay Attention To:
- Only swap rows inside the selected k x k submatrix
- Do not touch cells outside the square
- Use k // 2 because the middle row of an odd-sized square stays unchanged
- Remember this is a vertical flip, not a horizontal flip
"""

from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        half = k // 2

        for i in range(half):
            top = x + i
            bottom = x + k - 1 - i

            for c in range(k):
                grid[top][y + c], grid[bottom][y + c] = grid[bottom][y + c], grid[top][y + c]

        return grid


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print(sol.reverseSubmatrix(grid, 1, 1, 3))
    # Expected:
    # [
    #   [1, 2, 3, 4],
    #   [5, 14, 15, 16],
    #   [9, 10, 11, 12],
    #   [13, 6, 7, 8]
    # ]
