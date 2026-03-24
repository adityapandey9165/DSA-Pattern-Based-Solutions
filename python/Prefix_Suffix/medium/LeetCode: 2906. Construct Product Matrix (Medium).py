"""
LeetCode: 2906. Construct Product Matrix (Medium)
Problem Link: https://leetcode.com/problems/construct-product-matrix/
Author: Aditya Pandey
Date: 2026-03-24

------------------------------------------------------------
Problem:
Given a matrix grid, construct a new matrix where each cell contains
the product of all other cells in the matrix except the current cell,
modulo 12345.

------------------------------------------------------------
Pattern:
Prefix Product + Suffix Product
(Flattened traversal)

------------------------------------------------------------
How it works:
A brute-force approach would compute the product of all elements
for every cell separately, but that would be too slow and division
cannot be used safely under modulo.

Instead, we treat the matrix as a 1D array in row-major order:
- First pass: store prefix product before each cell
- Second pass: multiply by suffix product after each cell

For each cell:
    answer[cell] = product of all elements before it
                 * product of all elements after it

This gives the product of all other cells without using division.

------------------------------------------------------------
Why this works:
If we flatten the matrix:
    a1, a2, a3, ..., aN

Then for position i:
    product_except_i = (a1 * ... * a(i-1)) * (a(i+1) * ... * aN)

Prefix pass stores the left side.
Suffix pass stores the right side.
Multiplying both gives the final answer.

------------------------------------------------------------
Time Complexity:
O(m * n)

Space Complexity:
O(m * n) for the output matrix

------------------------------------------------------------
Things to Pay Attention To:
- Do NOT use division
- Use modulo 12345 at every multiplication
- Traverse in the correct order for prefix and suffix passes
- The matrix is handled in row-major order
"""

from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        row, col = len(grid), len(grid[0])

        res = [[1] * col for _ in range(row)]

        # Prefix product pass
        p = 1
        for r in range(row):
            for c in range(col):
                res[r][c] = p
                p = (p * grid[r][c]) % MOD

        # Suffix product pass
        p = 1
        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                res[r][c] = (res[r][c] * p) % MOD
                p = (p * grid[r][c]) % MOD

        return res


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.constructProductMatrix([[1, 2], [3, 4]]))
    # Expected:
    # [[24, 12],
    #  [8, 6]]

    print(sol.constructProductMatrix([[1, 5, 2], [3, 4, 6]]))
