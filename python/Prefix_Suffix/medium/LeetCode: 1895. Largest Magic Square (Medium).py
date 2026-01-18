"""
LeetCode: 1895. Largest Magic Square (Medium)
Problem Link: https://leetcode.com/problems/largest-magic-square/
Author: Aditya Pandey
Date: 16-01-2026

--------------------------------------------------
Problem:
Given a grid of integers, return the size of the largest magic square.

A k x k magic square satisfies:
- Sum of every row is equal
- Sum of every column is equal
- Sum of both diagonals is equal

--------------------------------------------------
Pattern:
Prefix Sum + Matrix Enumeration

--------------------------------------------------
Approach:
To efficiently check sums of rows, columns, and diagonals, we precompute:

1. Row prefix sum
2. Column prefix sum
3. Main diagonal prefix sum
4. Anti-diagonal prefix sum

For every possible top-left cell (r, c):
- Try all square sizes k (from 2 to max possible)
- Use prefix sums to validate:
  - All row sums
  - All column sums
  - Both diagonals
- Update result if a valid magic square is found

A 1x1 square is always magic.

--------------------------------------------------
Time Complexity:
O(m * n * min(m, n)^2)

Space Complexity:
O(m * n)

--------------------------------------------------
Things to Pay Attention:
- Prefix sum boundaries
- Diagonal calculations
- Early break on invalid square
--------------------------------------------------
"""

from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Row prefix sum
        rowSum = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                rowSum[r][c + 1] = rowSum[r][c] + grid[r][c]

        # Column prefix sum
        colSum = [[0] * n for _ in range(m + 1)]
        for c in range(n):
            for r in range(m):
                colSum[r + 1][c] = colSum[r][c] + grid[r][c]

        # Main diagonal prefix sum
        diag1 = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                diag1[r][c] = grid[r][c] + (diag1[r - 1][c - 1] if r > 0 and c > 0 else 0)

        # Anti-diagonal prefix sum
        diag2 = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n - 1, -1, -1):
                diag2[r][c] = grid[r][c] + (diag2[r - 1][c + 1] if r > 0 and c + 1 < n else 0)

        res = 1  # 1x1 square is always magic

        for r in range(m):
            for c in range(n):
                max_k = min(m - r, n - c)
                for k in range(2, max_k + 1):
                    target = rowSum[r][c + k] - rowSum[r][c]
                    ok = True

                    # Check rows
                    for i in range(r, r + k):
                        if rowSum[i][c + k] - rowSum[i][c] != target:
                            ok = False
                            break

                    # Check columns
                    if ok:
                        for j in range(c, c + k):
                            if colSum[r + k][j] - colSum[r][j] != target:
                                ok = False
                                break

                    # Check diagonals
                    if ok:
                        d1 = diag1[r + k - 1][c + k - 1] - (diag1[r - 1][c - 1] if r > 0 and c > 0 else 0)
                        d2 = diag2[r + k - 1][c] - (diag2[r - 1][c + k] if r > 0 and c + k < n else 0)
                        if d1 != target or d2 != target:
                            ok = False

                    if ok:
                        res = max(res, k)

        return res


# -----------------------
# Local Testing
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestMagicSquare([[7,1,4,5,6],
                                  [2,5,1,6,4],
                                  [1,5,4,3,2],
                                  [1,2,7,3,4]]))  # Expected: 3
