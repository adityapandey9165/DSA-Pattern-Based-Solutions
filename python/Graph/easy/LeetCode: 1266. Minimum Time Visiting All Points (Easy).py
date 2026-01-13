"""
LeetCode: 1266. Minimum Time Visiting All Points (Easy)
Problem link: https://leetcode.com/problems/minimum-time-visiting-all-points/
Author: Aditya Pandey
Date: 2026-01-13

Problem:
You are given a list of points on a 2D plane.
Moving from one point to another, you can:
- move vertically
- move horizontally
- move diagonally

Each move takes 1 unit of time.
Return the **minimum time** required to visit all points in the given order.

---

Approach: Greedy / Math Observation

Key observation:
- From point (x1, y1) to (x2, y2):
  - Horizontal distance = |x2 - x1|
  - Vertical distance   = |y2 - y1|
- You can move diagonally to cover both x and y simultaneously.

Therefore, the minimum time needed is:
    max(|x2 - x1|, |y2 - y1|)

We compute this for every consecutive pair of points and sum it up.

---

Why this works:
- Diagonal moves reduce both x and y by 1 per step.
- Once one axis is aligned, remaining movement is straight.
- Total steps = max(delta_x, delta_y)

---

Time Complexity:
- O(n), where n is the number of points

Space Complexity:
- O(1)
"""


from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            total_time += max(abs(x2 - x1), abs(y2 - y1))

        return total_time


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
    # Expected: 7

    print(sol.minTimeToVisitAllPoints([[3,2],[-2,2]]))
    # Expected: 5
