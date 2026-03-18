"""
LeetCode 1727 — Largest Submatrix With Rearrangements
Difficulty: Medium
Topic: Matrix, Greedy, Sorting

--------------------------------------------------

Problem
-------
Given a binary matrix, you can rearrange the columns
of each row independently.

Return the area of the largest submatrix consisting only of 1s.

--------------------------------------------------

Key Idea
--------
1. Convert grid into "heights" (like histogram)
   - Each cell stores consecutive 1s above it.

2. For each row:
   - Sort heights in descending order
   - Try forming submatrix using width = index + 1

3. Compute max area

--------------------------------------------------

Time Complexity
---------------
O(m * n log n)

Space Complexity
----------------
O(1) (in-place modification)

--------------------------------------------------
"""

from typing import List


class Solution:
    def largestSubmatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Step 1: Build heights (like histogram)
        for r in range(1, rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    grid[r][c] += grid[r - 1][c]

        max_area = 0

        # Step 2: Process each row
        for r in range(rows):
            heights = sorted(grid[r], reverse=True)

            for i in range(cols):
                width = i + 1
                area = heights[i] * width
                max_area = max(max_area, area)

        return max_area


# -------------------------------
# Local Testing
# -------------------------------
if __name__ == "__main__":
    sol = Solution()

    grid = [
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 1]
    ]

    print(sol.largestSubmatrix(grid))  # Expected Output: 4
