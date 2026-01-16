"""
LeetCode: 85. Maximal Rectangle (Hard)
Problem Link: https://leetcode.com/problems/maximal-rectangle/
Author: Aditya Pandey
Date: 2026-01-16

--------------------------------------------------
Problem Definition:
--------------------------------------------------
Given a 2D binary matrix filled with '0's and '1's,
find the largest rectangle containing only '1's
and return its area.

--------------------------------------------------
Approach:
--------------------------------------------------
This problem is an extension of:
"Largest Rectangle in Histogram"

Idea:
- Treat each row as the base of a histogram.
- Build a `height[]` array where:
    height[c] = number of consecutive '1's above (including current row)
- For every row, calculate the largest rectangle area
  using a monotonic increasing stack.

Steps:
1. Initialize a height array of size = number of columns.
2. For each row:
   - Update heights based on current row values.
   - Apply Largest Rectangle in Histogram logic.
3. Track and return the maximum area found.

--------------------------------------------------
Why Stack?
--------------------------------------------------
- Helps find nearest smaller bar on left and right.
- Ensures O(n) processing per row.

--------------------------------------------------
Time Complexity:
--------------------------------------------------
O(rows * cols)

--------------------------------------------------
Space Complexity:
--------------------------------------------------
O(cols)
"""


from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        row, col = len(matrix), len(matrix[0])
        height = [0] * col
        max_area = 0

        for r in range(row):
            # Build histogram
            for c in range(col):
                if matrix[r][c] == '1':
                    height[c] += 1
                else:
                    height[c] = 0

            # Largest Rectangle in Histogram
            stack = []
            for i in range(col + 1):
                curr = height[i] if i < col else 0

                while stack and curr < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)

                stack.append(i)

        return max_area


# -----------------------
# Quick sanity test
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(sol.maximalRectangle(matrix))  # Expected: 6
