"""
LeetCode: 128. Longest Consecutive Sequence (Medium)
Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/
Author: Aditya Pandey
Date: 2026-04-06

------------------------------------------------------------
Problem:
Given an unsorted array of integers nums, return the length of the
longest consecutive elements sequence.

You must solve it in O(n) time.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].

------------------------------------------------------------
Pattern:
HashSet + Sequence Start Detection

------------------------------------------------------------
Approach:
We store all numbers in a set for O(1) average lookup.

For each number x:
- If x - 1 is NOT in the set,
  then x is the start of a consecutive sequence.
- Expand forward:
    x, x+1, x+2, ...
  until the sequence breaks.

Track the maximum length found.

------------------------------------------------------------
Why this works:
If a number has a predecessor, it is not a sequence start.
So we only begin counting from true starts.
This prevents repeated work and keeps the solution O(n).

------------------------------------------------------------
Time Complexity:
O(n) average

Each number is visited at most twice:
- once while checking starts
- once while extending a sequence

------------------------------------------------------------
Space Complexity:
O(n)

We store all numbers in a hash set.

------------------------------------------------------------
Things to Pay Attention To:
- Convert nums to a set first
- Only start counting when x - 1 is missing
- Do not sort the array, that would be O(n log n)
- Handle duplicates naturally by using a set
- Empty array should return 0

------------------------------------------------------------
Common Mistakes:
- Starting from every number, which causes repeated counting
- Using sorting instead of hash set
- Forgetting to check x - 1 not in set
------------------------------------------------------------
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for i in nums:
            # only start from the beginning of a sequence
            if i - 1 not in nums:
                k = i
                while k in nums:
                    k += 1
                res = max(res, k - i)

        return res


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    # Expected: 4

    print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    # Expected: 9

    print(sol.longestConsecutive([]))
    # Expected: 0
