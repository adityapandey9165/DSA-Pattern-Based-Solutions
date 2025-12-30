"""
LeetCode: 840. Magic Squares in Grid (Medium)
Problem link: https://leetcode.com/problems/magic-squares-in-grid/
Author: Aditya Pandey
Date: 2025-12-30

Problem:
A 3 × 3 magic square is a grid filled with distinct numbers from 1 to 9
such that each row, column, and both diagonals sum to 15.

Given an m x n integer grid, return the number of 3 × 3 magic squares
contained in the grid.

---

Approach: Fixed Sliding Window (3×3) + Validation

We iterate over every possible 3 × 3 submatrix and validate whether it
satisfies the magic square properties.

Key optimizations and checks:
1. The center of a 3×3 magic square must be 5.
2. All numbers must be unique and exactly from 1 to 9.
3. Each row and each column must sum to 15.
4. Both diagonals must sum to 15.

If all conditions are satisfied, we count it as a valid magic square.

---

Why center must be 5:
- Numbers used are 1 to 9 → total sum = 45
- Each row/column sum = 15
- In a 3×3 magic square, only 5 can occupy the center position

This allows early pruning and avoids unnecessary checks.

---

Time Complexity: O(m × n)
Space Complexity: O(1)
"""


from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3:
            return 0

        def isMagic(r: int, c: int) -> bool:
            # Center must be 5
            if grid[r + 1][c + 1] != 5:
                return False

            # Collect all numbers in the 3x3 subgrid
            nums = [grid[r + i][c + j] for i in range(3) for j in range(3)]
            if set(nums) != set(range(1, 10)):
                return False

            # Check rows and columns
            for i in range(3):
                if sum(grid[r + i][c:c + 3]) != 15:
                    return False
                if sum(grid[r + j][c + i] for j in range(3)) != 15:
                    return False

            # Check diagonals
            if grid[r][c] + grid[r + 2][c + 2] != 15:
                return False
            if grid[r][c + 2] + grid[r + 2][c] != 15:
                return False

            return True

        count = 0
        for r in range(n - 2):
            for c in range(m - 2):
                if isMagic(r, c):
                    count += 1

        return count


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.numMagicSquaresInside([[4,3,8,4],
                                     [9,5,1,9],
                                     [2,7,6,2]]))
    # Expected: 1

    print(sol.numMagicSquaresInside([[8]]))
    # Expected: 0

    print(sol.numMagicSquaresInside([[10,3,5],
                                     [1,6,11],
                                     [7,9,2]]))
    # Expected: 0
