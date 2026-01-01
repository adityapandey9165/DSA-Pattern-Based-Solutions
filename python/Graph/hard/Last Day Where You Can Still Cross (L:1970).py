"""
LeetCode: 1970. Last Day Where You Can Still Cross (Hard)
Problem link: https://leetcode.com/problems/last-day-where-you-can-still-cross/
Author: Aditya Pandey
Date: 2025-12-30

Problem:
You are given integers `row` and `col` representing a grid of size row × col.
Cells are flooded day by day according to the array `cells`,
where cells[i] = [r, c] indicates that cell (r, c) is flooded on day i + 1.

You can start from any cell in the top row and move to adjacent cells
(up, down, left, right) that are not flooded.

Return the **latest day** when it is still possible to cross
from the top row to the bottom row.

---

Approach: Binary Search + BFS (Graph Traversal)

Key idea:
- Instead of simulating day-by-day, we **binary search on the answer** (day).
- For a given day `mid`, we check if crossing is possible using BFS.

Steps:
1. Preprocess the grid so that each cell stores the day it gets flooded.
2. Binary search on the day range [0, len(cells)].
3. For each mid:
   - Treat cells flooded on or before `mid` as blocked.
   - Run BFS from all valid cells in the top row.
   - If we reach the bottom row, crossing is possible.

---

Why Binary Search?
- The condition "can cross" is monotonic:
    - If crossing is possible on day `d`,
      it is also possible on all days `< d`.
- This allows binary search for the maximum valid day.

---

Time Complexity:
- Grid preprocessing: O(row × col)
- BFS check: O(row × col)
- Binary Search iterations: O(log(row × col))

Total: O((row × col) log(row × col))

Space Complexity:
- O(row × col) for visited set and queue
"""


from typing import List
from collections import deque


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # Grid stores the day on which each cell gets flooded
        grid = [[0] * col for _ in range(row)]
        day = 1
        for r, c in cells:
            grid[r - 1][c - 1] = day
            day += 1

        def canCross(mid: int) -> bool:
            """
            Check if crossing is possible on day = mid
            using BFS from top row to bottom row.
            """
            q = deque()
            visited = set()

            # Start BFS from all non-flooded cells in the top row
            for c in range(col):
                if grid[0][c] > mid:
                    q.append((0, c))
                    visited.add((0, c))

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < row and
                        0 <= nc < col and
                        (nr, nc) not in visited and
                        grid[nr][nc] > mid
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return False

        # Binary search on days
        left, right = 0, len(cells)
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if canCross(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.latestDayToCross(
        2, 2, [[1,1],[2,1],[1,2],[2,2]]
    ))
    # Expected: 2

    print(sol.latestDayToCross(
        3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
    ))
    # Expected: 3
