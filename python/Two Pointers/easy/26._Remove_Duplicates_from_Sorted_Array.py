"""
LeetCode: 26. Remove Duplicates from Sorted Array (Easy)
Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Author: Aditya Pandey
Date: 2025-09-04

Problem:
Given a sorted array nums, remove the duplicates in-place such that each element appears only once
and return the new length. Do not allocate extra space for another array; you must do this by
modifying the input array in-place with O(1) extra memory.

Pattern: Two Pointers (Slow / Fast) — In-place overwrite

Approach (Optimal - two pointers):
- Use a "slow" pointer k that tracks the position to write the next unique element.
- Use a "fast" pointer (loop variable) to scan the array.
- If nums[fast] != nums[k-1] (or k == 0), write nums[k] = nums[fast]; increment k.
- At the end, first k elements are the unique elements.

Why this is optimal:
- Only one pass over the array → O(n) time.
- Only constant extra memory (few pointers) → O(1) space.

Time Complexity: O(n)
Space Complexity: O(1)

Common Mistakes:
- Using a set to track seen elements (works but uses extra O(n) space; not allowed by the strict O(1) constraint).
- Shifting elements one-by-one (leads to O(n^2)).
- Off-by-one errors with pointer initialization.

Example Walkthrough:
nums = [1, 1, 2]
k = 0

fast = 0 -> x = 1, k == 0 -> nums[0] = 1, k = 1       => [1,1,2]
fast = 1 -> x = 1, x == nums[k-1] (1 == nums[0]) -> skip
fast = 2 -> x = 2, x != nums[k-1] (2 != nums[0]) -> nums[1] = 2, k = 2 => [1,2,2]

Result: k = 2, first k elements = [1,2]

---
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Optimal in-place solution using two pointers.
        Returns the length k of the array after removing duplicates; first k elements are unique.
        """
        k = 0  # next write position for a unique element
        for x in nums:
            # If k==0 (no elements written yet) or current x differs from last written element
            if k == 0 or x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k


# ---------- Optional: set-based version (works but uses O(n) extra space) ----------
def removeDuplicates_with_set(nums: List[int]) -> int:
    """
    Non-optimal variant using a set to track seen values.
    This preserves order and returns k, but uses O(n) extra space.
    Useful for understanding, but not the typical interview solution.
    """
    k = 0
    seen = set()
    for i in range(len(nums)):
        if nums[i] not in seen:
            nums[k] = nums[i]
            k += 1
        seen.add(nums[i])
    return k
# ---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Quick tests for revision / local verification
    sol = Solution()

    arr1 = [1, 1, 2]
    k1 = sol.removeDuplicates(arr1)
    print("k =", k1, "arr =", arr1[:k1])  # expected: k=2, arr=[1,2]

    arr2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = sol.removeDuplicates(arr2)
    print("k =", k2, "arr =", arr2[:k2])  # expected: k=5, arr=[0,1,2,3,4]
