"""
LeetCode: 27. Remove Element (Easy)
Problem link: https://leetcode.com/problems/remove-element/
Author: Aditya Pandey
Date: 2025-09-02

---
Problem:
Given an integer array nums and an integer val, remove all occurrences of val in-place.
The relative order of the elements may be changed. 
Return the number of elements in nums which are not equal to val.

---
Approach (Pattern: Two Pointers - Overwriting):
- Use two pointers:
  - i → scans the array
  - k → tracks where the next valid (non-val) element should be placed
- If nums[i] != val:
    → we copy nums[i] into nums[k]
    → then increment k
- If nums[i] == val:
    → we just skip it
- At the end, the first k elements in nums are the final array.

---
Example Walkthrough:
nums = [3, 2, 2, 3], val = 3

Initial:
k = 0
nums = [3, 2, 2, 3]

Step i=0 → nums[i] = 3 → equals val → skip
k = 0, nums unchanged

Step i=1 → nums[i] = 2 → not val → nums[k] = 2 → k=1
nums = [2, 2, 2, 3]

Step i=2 → nums[i] = 2 → not val → nums[k] = 2 → k=2
nums = [2, 2, 2, 3]

Step i=3 → nums[i] = 3 → equals val → skip
k = 2

Result: First k=2 elements → [2, 2]

---
Time Complexity: O(n)  (single pass)
Space Complexity: O(1) (in-place, no extra array)

Common Mistakes:
- Using nums.remove(val) in a loop → O(n^2), not efficient.
- Forgetting that we must overwrite nums[i] → result array might be wrong.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        In-place removal of val from nums.
        Returns the new length k (number of valid elements).
        """
        k = 0  # pointer to place next valid element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # overwrite at position k
                k += 1
        return k


if __name__ == "__main__":
    sol = Solution()
    
    nums = [3, 2, 2, 3]
    k = sol.removeElement(nums, 3)
    print("Final length:", k, "Remaining elements:", nums[:k])
    # Output: Final length: 2 Remaining elements: [2, 2]

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    k2 = sol.removeElement(nums2, 2)
    print("Final length:", k2, "Remaining elements:", nums2[:k2])
    # Output: Final length: 5 Remaining elements: [0, 1, 3, 0, 4]
