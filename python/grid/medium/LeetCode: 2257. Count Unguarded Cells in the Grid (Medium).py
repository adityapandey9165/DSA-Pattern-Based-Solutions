"""
LeetCode: 2257. Count Unguarded Cells in the Grid (Medium)
Problem link: https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
Author: Aditya Pandey
Date: 2025-11-02

Problem:
You are given two integers `m` and `n` representing the dimensions of a grid.
You are also given:
- `guards`: list of positions where guards are placed
- `walls`: list of positions where walls are placed

A guard can see in all 4 directions (up, down, left, right) until its view is 
blocked by either a wall or another guard.

Return the number of unguarded and unwalled cells.

Rules:
- A guard blocks the visibility of another guard in the same line.
- A wall blocks all visibility in its path.
- Only cells that are not guarded AND not walls should be counted.

Pattern: Grid + Directional Sweep (Simulation)

Approach:
1. Create a grid initialized with 0 meaning unoccupied.
2. Mark guards as "G" and walls as "W".
3. For each guard, move in 4 directions until blocked, marking visible cells as -1.
4. Count cells still equal to 0 at the end.

Time Complexity: O(m * n * 4) ≈ O(mn)
Space Complexity: O(m * n)
"""

from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        # Mark guards and walls
        for a, b in guards:
            grid[a][b] = "G"
        for a, b in walls:
            grid[a][b] = "W"

        # Directions: up, down, left, right
        dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Mark guarded cells
        for r, c in guards:
            for dr, dc in dirr:
                i, j = r + dr, c + dc
                while 0 <= i < m and 0 <= j < n:
                    if grid[i][j] in ("W", "G"):
                        break
                    if grid[i][j] == 0:
                        grid[i][j] = -1  # Mark as guarded
                    i += dr
                    j += dc

        # Count unguarded cells
        res = sum(val == 0 for row in grid for val in row)
        return res


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]))  # 7
    print(sol.countUnguarded(3, 3, [[0,0],[1,1],[2,2]], []))  # 0
    print(sol.countUnguarded(2, 7, [[1,5],[1,1],[1,6],[0,2]], [[0,6],[0,3],[0,5]]))  # 3
