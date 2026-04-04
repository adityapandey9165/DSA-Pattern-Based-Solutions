"""
LeetCode: 2075. Decode the Slanted Ciphertext (Medium)
Problem Link: https://leetcode.com/problems/decode-the-slanted-ciphertext/
Author: Aditya Pandey
Date: 2026-04-04

------------------------------------------------------------
Problem:
You are given a string encodedText and an integer row.

The text was written in a matrix with `row` rows by placing the original
message row by row, then reading it diagonally from top-left to bottom-right.

Your task is to decode the original text.

Return the decoded string after removing trailing spaces.

------------------------------------------------------------
Pattern:
Matrix Simulation + Diagonal Traversal

------------------------------------------------------------
Approach:
1. The encoded text was written into a matrix row by row.
2. Reconstruct the matrix with:
   - number of rows = row
   - number of columns = len(encodedText) // row
3. Read the matrix diagonally starting from each column of the first row:
   - start at (0, c)
   - move down-right until going out of bounds
4. Collect all characters in order.
5. Remove trailing spaces using rstrip().

------------------------------------------------------------
Why this works:
The encoding process places the original text in a grid and then
reads diagonals. So to decode, we reverse that process:
- rebuild the grid
- traverse each diagonal in the same order used by encoding

------------------------------------------------------------
Time Complexity:
O(m * n)
where m = row, n = number of columns

Space Complexity:
O(m * n)
for the matrix

------------------------------------------------------------
Things to Pay Attention To:
- The matrix is filled row by row
- Diagonal traversal must go down-right
- Use rstrip() to remove trailing spaces
- Do not forget that encodedText may contain spaces
------------------------------------------------------------
"""

from typing import List


class Solution:
    def decodeCiphertext(self, encodedText: str, row: int) -> str:
        if row == 1:
            return encodedText.rstrip()

        cols = len(encodedText) // row
        mat = [[""] * cols for _ in range(row)]

        idx = 0
        for r in range(row):
            for c in range(cols):
                mat[r][c] = encodedText[idx]
                idx += 1

        def go_down(r: int, c: int) -> list[str]:
            chars = []
            while r < row and c < cols:
                chars.append(mat[r][c])
                r += 1
                c += 1
            return chars

        res = []
        for c in range(cols):
            res.extend(go_down(0, c))

        return "".join(res).rstrip()


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.decodeCiphertext("ch   ie   pr", 3))
    # Expected: "cipher"

    print(sol.decodeCiphertext("iveo    eed   l te   olc", 4))
    # Expected: "i love leetcode"

    print(sol.decodeCiphertext("coding", 1))
    # Expected: "coding"
