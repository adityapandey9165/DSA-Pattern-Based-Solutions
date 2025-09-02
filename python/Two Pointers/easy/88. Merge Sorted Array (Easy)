"""
LeetCode: 88. Merge Sorted Array (Easy)
Problem link: https://leetcode.com/problems/merge-sorted-array/
Author: Aditya Pandey
Date: 2025-09-02

Problem:
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The first array nums1 has a length of m + n, where the first m elements denote the elements
that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has
length n and contains n elements to merge into nums1.

Approach:
- Use three pointers (i, j, k) starting from the end:
  - i -> last valid element in nums1 (index m-1)
  - j -> last element in nums2 (index n-1)
  - k -> last position in nums1 (index m+n-1)
- Compare nums1[i] and nums2[j], place the larger at nums1[k], and move pointers accordingly.
- Continue until all elements of nums2 have been placed.
- This in-place approach avoids extra memory and runs in O(m + n) time.

Time Complexity: O(m + n) where m = number of initial elements in nums1, n = len(nums2)
Space Complexity: O(1) extra space (in-place)

Common Mistakes:
- Inserting elements at the front or shifting elements repeatedly (leads to O(n^2)).
- Forgetting to copy the remaining elements from nums2 when i runs out.
- Off-by-one errors with indices (remember zero-based indexing and that k starts at m + n - 1).
- Modifying nums1 while iterating forward (use backward pointers to avoid overwriting useful data).
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place. nums1 has length m + n with trailing zeros.
        After this function, nums1 should contain the merged sorted array.
        """

        # Pointers:
        # i -> last valid element in the original nums1 (index m-1)
        # j -> last element in nums2 (index n-1)
        # k -> last position in nums1 (index m+n-1)
        i = m - 1
        j = n - 1
        k = m + n - 1

        # Merge in reverse order so we don't overwrite elements in nums1 we haven't processed.
        while i >= 0 and j >= 0:
            # Place the larger of nums1[i] and nums2[j] at nums1[k]
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2 (nums1's remaining elements are already in place),
        # copy them. (If j < 0, nothing left in nums2.)
        
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


if __name__ == "__main__":
    # Quick manual test (can be expanded to proper pytest tests in repo)
    sol = Solution()
    a = [1, 2, 3, 0, 0, 0]
    sol.merge(a, 3, [2, 5, 6], 3)
    print(a)  # expected: [1, 2, 2, 3, 5, 6]

    b = [0]
    sol.merge(b, 0, [1], 1)
    print(b)  # expected: [1]
