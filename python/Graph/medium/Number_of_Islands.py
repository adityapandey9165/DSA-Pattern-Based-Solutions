"""
LeetCode: 200. Number of Islands (Medium)
Problem link: https://leetcode.com/problems/number-of-islands/
Author: Aditya Pandey
Date: 2025-09-08

Problem:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are surrounded by water.

Pattern: Graph Traversal (DFS / BFS Flood Fill)

Approach 1: DFS
- Iterate through each cell in the grid.
- If we find '1' (land), it means we found a new island.
- Use DFS to mark all connected land cells ('1') as '0' (visited).
- Continue until the entire grid is processed.
- Count how many times DFS is called = number of islands.

Approach 2: BFS
- Instead of recursion, use a queue to explore neighbors (iterative).
- Works better when recursion depth could cause stack overflow.

Time Complexity: O(m * n)  → Each cell visited once
Space Complexity:
- DFS: O(m * n) recursion stack (worst case)
- BFS: O(min(m,n)) for queue (in practice)

Common Interview Questions:
1. Can you implement both DFS and BFS? (iterative vs recursive)
2. What happens if the grid is very large? (stack overflow in DFS)
3. Can we do it in-place without extra visited array? (yes → mark visited as '0')
4. How would the solution change if diagonals also counted as neighbors?
5. How to handle huge grids (like streaming input)? → Union-Find (DSU) approach
6. Follow-up: Count the **maximum area of an island** instead of just the number.

Example:
Input: 
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""

from typing import List
from collections import deque

class Solution:
    # DFS version
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # mark visited
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        return islands


class SolutionBFS:
    # BFS version
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = '0'
            while q:
                x, y = q.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = x + dx, y + dy
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        q.append((nr, nc))

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        return islands
