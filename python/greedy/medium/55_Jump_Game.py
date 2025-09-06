"""
LeetCode: 55. Jump Game (Medium)
Problem link: https://leetcode.com/problems/jump-game/
Author: Aditya Pandey
Date: 2025-09-06

Problem:
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return True if you can reach the last index, or False otherwise.

Pattern: Greedy (Right-to-Left Greedy / Last Good Position)

Approach:
- Maintain a variable `goal` that stores the smallest index known so far from which
  the end is reachable. Initialize `goal = n - 1` (the last index).
- Traverse the array from right to left (i = n-1 down to 0):
  - If i + nums[i] >= goal, then index i can reach `goal`, so update `goal = i`.
- After the loop, if `goal == 0`, the start index can reach the end; return True.
- Otherwise return False.

Why this works (intuition):
- We track the nearest index that can reach the end. Any index that can reach that
  index can also reach the end. By moving leftwards we "shrink" the goal to earlier
  indices whenever possible.

Time Complexity: O(n) — single pass from right to left.
Space Complexity: O(1) — constant extra space.

Common Mistakes:
- Returning `nums[0] >= goal` (incorrect check).
- Trying naive DFS/backtracking without memoization — can be slow.
- Using left-to-right greedy incorrectly (it can be done but is trickier).
- Off-by-one errors when computing reachable index (remember i + nums[i]).

Example Walkthrough:
nums = [2,3,1,1,4]
n = 5, goal = 4

i = 4 -> 4 + nums[4] = 4 >= goal(4) -> goal = 4
i = 3 -> 3 + nums[3] = 4 >= goal(4) -> goal = 3
i = 2 -> 2 + nums[2] = 3 >= goal(3) -> goal = 2
i = 1 -> 1 + nums[1] = 4 >= goal(2) -> goal = 1
i = 0 -> 0 + nums[0] = 2 >= goal(1) -> goal = 0

goal == 0 -> True (start can reach end)

Edge case:
nums = [3,2,1,0,4]
Walking right-to-left:
goal stays at 4 until i=3: 3+0 < 4 so goal unchanged -> eventually goal != 0 -> False

"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Return True if we can reach the last index from the first index.
        Greedy: maintain rightmost (smallest index) reachable goal.
        """
        n = len(nums)
        if n <= 1:
            return True

        goal = n - 1
        # traverse from right to left
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


if __name__ == "__main__":
    # quick tests for revision
    sol = Solution()

    tests = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([2, 0, 0], True),
        ([1, 2, 3], True),
    ]

    for arr, expected in tests:
        res = sol.canJump(arr)
        print(f"nums={arr}  -> canJump={res} (expected={expected})")
