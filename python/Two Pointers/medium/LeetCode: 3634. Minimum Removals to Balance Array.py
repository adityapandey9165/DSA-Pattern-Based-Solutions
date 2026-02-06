"""
LeetCode: 3634. Minimum Removals to Balance Array
Date: 06/02/2026
Author: Aditya Pandey

Problem:
You are given an integer array nums and an integer k.
Remove the minimum number of elements so that in the remaining array,
max_element <= k * min_element.

Key observation:
Instead of thinking about removals, think about:
➡️ Keeping the largest possible subset that satisfies:
   max <= k * min
Answer = n - size_of_largest_valid_subset

------------------------------------------------
Pattern:
Sorting + Sliding Window
- Binary Search on sorted array
- Two Pointers (optimal sliding window)

Why sorting?
Once sorted, if nums[r] <= k * nums[l], then all elements between l and r
also satisfy the condition.
------------------------------------------------
"""

from typing import List
import bisect


class Solution:

    # =====================================================
    # Approach 1: Sorting + Binary Search
    # =====================================================
    # Idea:
    # - Sort the array
    # - For each index l, find the farthest index r such that
    #   nums[r] <= nums[l] * k using binary search
    #
    # Time Complexity:
    # - Sorting: O(n log n)
    # - For each l, binary search: O(log n)
    # - Total: O(n log n)
    #
    # Space Complexity:
    # - O(1) extra space (ignoring sort)
    #
    def minRemoval_binarySearch(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        max_keep = 0

        for l in range(n):
            limit = nums[l] * k
            r = bisect.bisect_right(nums, limit)
            max_keep = max(max_keep, r - l)

        return n - max_keep


    # =====================================================
    # Approach 2: Sorting + Two Pointers (Optimal)
    # =====================================================
    # Idea:
    # - Sort the array
    # - Use a sliding window [l, r)
    # - Expand r while condition holds
    # - r never moves backward → linear scan
    #
    # Time Complexity:
    # - Sorting: O(n log n)
    # - Sliding window: O(n)
    # - Total: O(n log n)
    #
    # Space Complexity:
    # - O(1) extra space
    #
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        max_keep = 0
        r = 0

        for l in range(n):
            if r < l:
                r = l

            while r < n and nums[r] <= nums[l] * k:
                r += 1

            max_keep = max(max_keep, r - l)

        return n - max_keep


"""
------------------------------------------------
Things people commonly miss (IMPORTANT)
------------------------------------------------
1. Forgetting to sort:
   ❌ Sliding window does NOT work on unsorted arrays.

2. Off-by-one error:
   - r is always the first index that breaks the condition
   - Window size = r - l (NOT r - l + 1)

3. Resetting r for every l:
   ❌ Makes solution O(n^2)
   ✅ r should only move forward

4. Integer overflow (in other languages):
   - nums[l] * k can overflow int
   - Use long / int64 in C++ / Java

5. Edge cases:
   - n == 0 → answer is 0
   - k == 0 → only zeros can remain
   - Duplicates are valid and handled naturally

------------------------------------------------
Which approach to use in interviews?
------------------------------------------------
- Explain Binary Search first (clear logic)
- Then say:
  "We can optimize this to O(n) using two pointers
   because r never moves backward."

That shows optimization thinking 👍
------------------------------------------------
"""
