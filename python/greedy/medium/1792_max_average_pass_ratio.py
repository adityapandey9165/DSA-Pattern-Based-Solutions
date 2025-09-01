"""
Leetcode:1792. Maximum Average Pass Ratio(Medium)
Problem link:https://leetcode.com/problems/maximum-average-pass-ratio/description/?envType=daily-question&envId=2025-09-01
Author: Aditya Pandey
Date: 2025-09-01

Problem:
Given classes = [[pass_i, total_i]] and extraStudents who will pass, assign students
to maximize average pass ratio.

Approach:
- Use a max-heap to always allocate an extra student to the class 
  that gains the most increase in pass ratio.
- Python's heapq is a min-heap by default, so we push negative gain 
  values to simulate a max-heap.
- After assigning all extra students, calculate the final average ratio.

Time Complexity: O((n + m) log n) where n = classes, m = extraStudents
Space Complexity: O(n)

Common Mistakes:
- Using the least ratio class instead of max gain class.
- Forgetting to update the heap after adding a student.
- Not handling Python's default min-heap (hence we use -gain).
"""

import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(a: int, b: int) -> float:
            return (a + 1) / (b + 1) - (a / b)

        h = []
        for a, b in classes:
            heapq.heappush(h, (-gain(a, b), a, b))
      
        for _ in range(extraStudents):
            _, a, b = heapq.heappop(h)
            a += 1
            b += 1
            heapq.heappush(h, (-gain(a, b), a, b))

        return sum(a / b for _, a, b in h) / len(classes)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2))  # ~0.7833
