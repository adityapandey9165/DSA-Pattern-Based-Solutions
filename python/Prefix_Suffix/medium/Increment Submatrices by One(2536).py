"""
LeetCode: 2536. Increment Submatrices by One (Medium)
Problem link: https://leetcode.com/problems/increment-submatrices-by-one/
Author: Aditya Pandey
Date: 2025-11-14

Problem:
You are given an integer n representing an n x n matrix initially filled with zeroes.
You are also given a list of queries, where each query is of the form:
    [r1, c1, r2, c2]

For each query, increment by 1 all elements in the submatrix with:
- top-left corner  = (r1, c1)
- bottom-right     = (r2, c2)

Return the final matrix after applying all queries.

---

Approach: 2D Difference Array + Prefix Sum

Instead of directly updating every cell in each submatrix (which could be slow),
we use a **difference matrix** `diff` that allows rectangle updates in O(1):

For each query (r1, c1, r2, c2):
    diff[r1][c1] += 1
    diff[r1][c2+1] -= 1            (if inside bounds)
    diff[r2+1][c1] -= 1            (if inside bounds)
    diff[r2+1][c2+1] += 1          (if inside bounds)

After processing all queries:
1. Take row-wise prefix sums
2. Take column-wise prefix sums

This reconstructs the final incremented matrix.

Why this works:
The 2D difference array is the extension of the 1D range-add trick:
- In 1D, to add +v on range [l, r], do:
      diff[l] += v
      diff[r+1] -= v
- After prefix sum, the entire segment [l, r] becomes +v.

In 2D, we mark changes at the corners so that when both horizontal and vertical
prefix sums are applied, the interior of the rectangle gets +1 while the outside
cancels out.

---

Time Complexity: O(n² + q)
Space Complexity: O(n²)
"""

from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * n for _ in range(n)]

        # Apply corner difference updates
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            if c2 + 1 < n:
                diff[r1][c2 + 1] -= 1
            if r2 + 1 < n:
                diff[r2 + 1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                diff[r2 + 1][c2 + 1] += 1

        # Row-wise prefix sums
        for r in range(n):
            for c in range(1, n):
                diff[r][c] += diff[r][c - 1]

        # Column-wise prefix sums
        for c in range(n):
            for r in range(1, n):
                diff[r][c] += diff[r - 1][c]

        return diff


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]]))
    # Expected: [[1,1,0],[1,2,1],[0,1,1]]

    print(sol.rangeAddQueries(2, [[0,0,1,1]]))
    # Expected: [[1,1],[1,1]]

    print(sol.rangeAddQueries(4, [[0,0,3,3],[1,1,2,2]]))
    # Expected: [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
