"""
LeetCode: 1594. Maximum Non Negative Product in a Matrix (Medium)
Problem Link: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/
Author: Aditya Pandey
Date: 2026-03-23

------------------------------------------------------------
Problem
------------------------------------------------------------
You are given a matrix grid.

You can move only:
- Right
- Down

You need to find the maximum product path from (0,0) to (m-1,n-1).

Return:
- max product % (1e9+7) if >= 0
- else return -1

------------------------------------------------------------
Pattern
------------------------------------------------------------
Dynamic Programming on Grid
(Tracking BOTH max and min)

------------------------------------------------------------
Key Insight
------------------------------------------------------------
Because of negative numbers:

(-ve) * (-ve) = (+ve)

So we must track:
- max product till cell
- min product till cell

------------------------------------------------------------
Approach
------------------------------------------------------------

At each cell (r, c):

We can come from:
- top (r-1, c)
- left (r, c-1)

So candidates are:

max_dp[r-1][c] * val
max_dp[r][c-1] * val
min_dp[r-1][c] * val
min_dp[r][c-1] * val

Take:
max → for max_dp
min → for min_dp

------------------------------------------------------------
Initialization
------------------------------------------------------------

First row and column:
only one path → multiply directly

------------------------------------------------------------
Time Complexity
------------------------------------------------------------
O(m * n)

------------------------------------------------------------
Space Complexity
------------------------------------------------------------
O(m * n)

------------------------------------------------------------
Common Mistakes
------------------------------------------------------------
1. Not tracking min → WRONG
2. Handling negative numbers incorrectly
3. Forgetting modulo condition at end
4. Returning negative instead of -1
------------------------------------------------------------
"""

from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]

        max_dp[0][0] = grid[0][0]
        min_dp[0][0] = grid[0][0]

        # First column
        for i in range(1, m):
            max_dp[i][0] = max_dp[i - 1][0] * grid[i][0]
            min_dp[i][0] = max_dp[i][0]

        # First row
        for j in range(1, n):
            max_dp[0][j] = max_dp[0][j - 1] * grid[0][j]
            min_dp[0][j] = max_dp[0][j]

        # Fill DP
        for r in range(1, m):
            for c in range(1, n):
                val = grid[r][c]

                candidates = [
                    max_dp[r - 1][c] * val,
                    max_dp[r][c - 1] * val,
                    min_dp[r - 1][c] * val,
                    min_dp[r][c - 1] * val
                ]

                max_dp[r][c] = max(candidates)
                min_dp[r][c] = min(candidates)

        res = max_dp[m - 1][n - 1]

        MOD = 10**9 + 7

        return res % MOD if res >= 0 else -1


# -----------------------
# Quick Test
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
    print(sol.maxProductPath(grid))  # Expected: 8
