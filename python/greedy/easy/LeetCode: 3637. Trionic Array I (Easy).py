"""
LeetCode: 3637. Trionic Array I (Easy)
Problem Link: https://leetcode.com/problems/trionic-array-i/
Author: Aditya Pandey
Date: 2026-03-26

--------------------------------------------------
Pattern:
Greedy + One-Pass Three-Phase Scan

--------------------------------------------------
Approach:
A trionic array must have **three non-empty segments**:
1) strictly increasing
2) strictly decreasing
3) strictly increasing

We explicitly walk these three phases in order.

Steps:
1. Walk forward while array is strictly increasing
   → this defines index p
2. Walk forward while array is strictly decreasing
   → this defines index q
3. Walk forward while array is strictly increasing again
4. At the end, ensure:
   - all elements are used
   - each segment had at least one step

--------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(1)

--------------------------------------------------
Things People Miss:
1. Equal adjacent values are NOT allowed
2. Each segment must be non-empty
3. Order must be inc → dec → inc (no extra changes)
--------------------------------------------------
"""

from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        i = 0

        # 1️⃣ strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:              # no increasing part
            return False
        p = i

        # 2️⃣ strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == p:              # no decreasing part
            return False
        q = i

        # 3️⃣ strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == q:              # no final increasing part
            return False

        # must consume entire array
        return i == n - 1


# -----------------------
# Quick sanity tests
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.isTrionic([1, 3, 5, 4, 2, 6, 8]))   # True
    print(sol.isTrionic([1, 2, 3, 4]))            # False
    print(sol.isTrionic([1, 3, 2, 4, 3]))         # False
    print(sol.isTrionic([1, 3, 2, 4]))            # True
    print(sol.isTrionic([1, 3, 3, 2, 4]))         # False (equal values)
