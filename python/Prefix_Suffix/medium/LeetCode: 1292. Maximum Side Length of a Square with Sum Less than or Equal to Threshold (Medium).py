"""
LeetCode: 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold (Medium)
Problem link: https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
Author: Aditya Pandey
Date: 2026-01-19

Problem:
Given a matrix of integers and an integer threshold, return the maximum side-length of a
square with sum less than or equal to threshold. If no such square exists, return 0.

Approach: 2D Prefix Sum + Binary Search on side length

Key ideas:
1. Build a 2D prefix sum array `prefix` with shape (rows+1) x (cols+1):
   prefix[i+1][j+1] = sum of matrix elements in rectangle from (0,0) to (i,j).
2. A k × k square with bottom-right prefix index (r, c) (1-based in prefix) has sum:
   sum = prefix[r][c] - prefix[r-k][c] - prefix[r][c-k] + prefix[r-k][c-k]
3. Binary search on possible side length `k` in range [0, min(rows, cols)]:
   - For a candidate `k`, check if any k×k square has sum ≤ threshold using prefix sums.
   - If yes, try larger k; otherwise try smaller.

Time Complexity:
- Building prefix: O(rows * cols)
- For each binary-search step, checking all squares: O(rows * cols)
- Binary-search steps: O(log(min(rows, cols)))
→ Total: O(rows * cols * log(min(rows, cols)))

Space Complexity:
- O(rows * cols) for prefix array
"""


from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if not mat or not mat[0]:
            return 0

        rows, cols = len(mat), len(mat[0])

        # Build (rows+1) x (cols+1) prefix sum array
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                # standard 2D prefix sum formula
                prefix[i + 1][j + 1] = (
                    prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j] + mat[i][j]
                )

        def valid(k: int) -> bool:
            """Return True if there exists a k x k square with sum <= threshold."""
            if k == 0:
                return True
            # iterate over bottom-right corner indices in prefix (1..rows, 1..cols)
            for r in range(k, rows + 1):
                for c in range(k, cols + 1):
                    s = (
                        prefix[r][c]
                        - prefix[r - k][c]
                        - prefix[r][c - k]
                        + prefix[r - k][c - k]
                    )
                    if s <= threshold:
                        return True
            return False

        low, high = 0, min(rows, cols)
        res = 0
        while low <= high:
            mid = (low + high) // 2
            if valid(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.maxSideLength([[1, 1, 3, 2, 4, 3], [1, 1, 3, 2, 4, 3], [1, 1, 3, 2, 4, 3]], 4))
    # Expected: 2

    print(sol.maxSideLength([[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], 1))
    # Expected: 0
