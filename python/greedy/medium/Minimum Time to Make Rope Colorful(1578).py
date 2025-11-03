"""
LeetCode: 1578. Minimum Time to Make Rope Colorful (Medium)
Problem link: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
Author: Aditya Pandey
Date: 2025-11-02

Problem:
You are given a string `colors` where each character represents the color of a balloon.
You are also given an integer array `neededTime`, where `neededTime[i]` is the time needed
to remove the i-th balloon.

You want to remove balloons so that no two adjacent balloons have the same color.
Return the minimum total time required to achieve this.

Rules:
- If two adjacent balloons have the same color, you must remove one.
- To minimize time, remove the one with smaller neededTime.
- Keep the balloon with the maximum cost in every same-color group.

Pattern: Greedy + Adjacent Comparison

Approach:
1. Track a running group of same-color balloons.
2. Compare current balloon with previous:
   - If same color → add the smaller cost to result, keep the larger cost.
   - If different color → reset group max.
3. Return total time of removals.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        cur_max = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                res += min(cur_max, neededTime[i])
                cur_max = max(cur_max, neededTime[i])
            else:
                cur_max = neededTime[i]

        return res


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.minCost("abaac", [1,2,3,4,5]))  # 3
    print(sol.minCost("abc", [1,2,3]))  # 0
    print(sol.minCost("aabaa", [1,2,3,4,1]))  # 2
