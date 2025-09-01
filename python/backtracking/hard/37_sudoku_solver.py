"""
Leetcode: 37. Sudoku Solver (Hard)
Problem link: https://leetcode.com/problems/sudoku-solver/description/
Author: Aditya Pandey
Date: 2025-09-01

Problem:
Given a partially filled 9x9 Sudoku board, fill the empty cells ('.') 
such that each row, each column, and each 3x3 sub-box contains 
digits 1–9 exactly once.

Approach:
- Use Backtracking (DFS):
  1. Find an empty cell.
  2. Try placing digits 1–9.
  3. Check validity: no duplicate in row, col, or 3x3 box.
  4. If valid, recurse to solve the next cell.
  5. If stuck, backtrack and try another digit.
- Stop when the board is completely filled.

Time Complexity: O(9^(n)) worst-case, where n = number of empty cells.
Space Complexity: O(n) recursion depth.

Common Mistakes:
- Forgetting to backtrack (reset cell after trying a digit).
- Not validating sub-boxes properly.
- Infinite recursion when no base case is handled.
"""

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(r, c, ch):
            # Check row
            for i in range(9):
                if board[r][i] == ch:
                    return False
            # Check column
            for i in range(9):
                if board[i][c] == ch:
                    return False
            # Check 3x3 subgrid
            box_r, box_c = 3 * (r // 3), 3 * (c // 3)
            for i in range(box_r, box_r + 3):
                for j in range(box_c, box_c + 3):
                    if board[i][j] == ch:
                        return False
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for ch in map(str, range(1, 10)):
                            if isValid(r, c, ch):
                                board[r][c] = ch
                                if solve():
                                    return True
                                board[r][c] = "."  # Backtrack
                        return False
            return True

        solve()


if __name__ == "__main__":
    sudoku = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    sol = Solution()
    sol.solveSudoku(sudoku)
    for row in sudoku:
        print(row)
