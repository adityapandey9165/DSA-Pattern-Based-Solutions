"""
LeetCode: 45. Jump Game II (Hard)
Problem link: https://leetcode.com/problems/jump-game-ii/
Author: Aditya Pandey
Date: 2025-09-06

Problem:
Given an array of non-negative integers nums where nums[i] represents the maximum
jump length from that position, return the minimum number of jumps required to
reach the last index. You can assume you can always reach the last index.

Pattern: Greedy / Range Expansion (BFS-like levels)

Approach:
- Think of ranges as levels: starting range [l, r] are indices reachable with `res` jumps.
- For each range, compute `farthest` = the maximum index we can reach from any index in [l, r].
- After scanning [l, r], move to the next range [r+1, farthest] and increment `res` (one more jump).
- Repeat until the right boundary `r` reaches or passes the last index.
- This is a greedy, BFS-like approach that runs in O(n) time.

Time Complexity: O(n) — each index visited at most once in the inner loop total.
Space Complexity: O(1) — constant extra space.

Common Mistakes:
- Using naive DP / BFS with O(n^2) complexity.
- Off-by-one errors when updating l and r boundaries.
- Not handling trivial case n == 1 (0 jumps needed).

Example Walkthrough:
nums = [2,3,1,1,4]
n=5
Initial: l=0, r=0, res=0
Level 1 (indices 0..0): farthest = max(0+2)=2 -> next range [1,2], res=1
Level 2 (indices 1..2): farthest = max(1+3, 2+1) = 4 -> next range [3,4], res=2
Now r >= n-1 -> answer res = 2

"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Return the minimum number of jumps to reach the last index.
        Greedy range-expansion approach.
        """
        n = len(nums)
        if n <= 1:
            return 0

        l = r = 0  # current window [l, r] reachable with `res` jumps
        res = 0

        # While the right boundary hasn't reached the last index
        while r < n - 1:
            farthest = 0
            # Expand within the current window to find farthest reachable index
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            # Move to next window (one more jump)
            l = r + 1
            r = farthest
            res += 1

        return res


if __name__ == "__main__":
    # quick tests for revision
    sol = Solution()
    tests = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([1], 0),
        ([1, 2], 1),
        ([2, 0, 2, 0, 1], 2),
    ]

    for arr, expected in tests:
        out = sol.jump(arr)
        print(f"nums={arr} -> jumps={out} (expected={expected})")
