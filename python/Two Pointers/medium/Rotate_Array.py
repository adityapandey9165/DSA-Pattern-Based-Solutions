"""
LeetCode: 189. Rotate Array (Medium)
Problem link: https://leetcode.com/problems/rotate-array/
Author: Aditya Pandey
Date: 2025-09-04

Problem:
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
The operation must be done in-place with O(1) extra space.

Pattern: Array Manipulation — Reverse Technique

Approach:
- Rotating right by k means the last k elements move to the front.
- Instead of shifting elements one by one (O(n*k)), we use reversal:
  1. Reverse the entire array.
  2. Reverse the first k elements.
  3. Reverse the last n-k elements.
- This achieves the rotation in-place with O(n) time and O(1) extra space.

Time Complexity: O(n) — Each element reversed at most twice.
Space Complexity: O(1) — In-place reversal.

Common Mistakes:
- Forgetting to handle k > n (solution: use k % n).
- Misplacing indices during reverse boundaries.
- Assuming extra array space is allowed (not in this problem).

Example Walkthrough:
nums = [1,2,3,4,5,6,7], k = 3
n = 7, k = 3 % 7 = 3

Step 1: Reverse whole array -> [7,6,5,4,3,2,1]
Step 2: Reverse first 3 -> [5,6,7,4,3,2,1]
Step 3: Reverse rest (indices 3..6) -> [5,6,7,1,2,3,4]

Result: [5,6,7,1,2,3,4]
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array nums to the right by k steps in-place.
        """
        n = len(nums)
        k = k % n  # Handle cases where k > n

        # Helper function: reverse elements between l and r
        def rev(l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # Step 1: Reverse the entire array
        rev(0, n - 1)

        # Step 2: Reverse first k elements
        rev(0, k - 1)

        # Step 3: Reverse remaining n-k elements
        rev(k, n - 1)


if __name__ == "__main__":
    # quick tests for revision
    sol = Solution()

    arr1 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(arr1, 3)
    print("arr1 =", arr1)  # expected: [5,6,7,1,2,3,4]

    arr2 = [-1, -100, 3, 99]
    sol.rotate(arr2, 2)
    print("arr2 =", arr2)  # expected: [3,99,-1,-100]

    arr3 = [1, 2]
    sol.rotate(arr3, 3)
    print("arr3 =", arr3)  # expected: [2,1]

    arr4 = [1]
    sol.rotate(arr4, 0)
    print("arr4 =", arr4)  # expected: [1]
