"""
LeetCode: 15. 3Sum (Medium)
Problem link: https://leetcode.com/problems/3sum/
Author: Aditya Pandey
Date: 2025-09-24

Problem:
Given an integer array nums, return all unique triplets [a,b,c] such that
a + b + c == 0. The solution set must not contain duplicate triplets.

Pattern: Sort + Two Pointers (fix one element, two-sum on the rest)

Approach (step-by-step):
1. Sort nums.
2. Iterate i from 0 to n-3 as the first element of the triplet.
   - Skip duplicates for i (if nums[i] == nums[i-1]).
   - If nums[i] > 0, break early (since further values are >= nums[i] and sum cannot be 0).
3. For each i, use two pointers left = i+1, right = n-1:
   - Compute total = nums[i] + nums[left] + nums[right].
   - If total == 0: record the triplet, then move left and right past duplicates.
   - If total < 0: left += 1 (need bigger sum).
   - If total > 0: right -= 1 (need smaller sum).
4. Continue until left >= right.
5. Return list of unique triplets.

Time Complexity: O(n^2) — dominated by the two-pointer scan for each i.
Space Complexity: O(log n) or O(n) depending on sorting implementation + O(k) for result.

Common Mistakes:
- Forgetting to skip duplicates for `i`, `left`, and `right` (causes duplicate triplets).
- Not breaking early when `nums[i] > 0` (minor optimization).
- Using a hashset of triplets without sorting — correct but less efficient and messy.
- Off-by-one errors in pointer movement when skipping duplicates.

Why this works:
- Sorting lets us use two-pointer technique to find pairs that sum to `-nums[i]` in linear time.
- Skipping duplicates ensures each unique triplet is selected exactly once.

"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n - 2):
            # skip duplicates for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # early break: if current number > 0, no triplet can sum to 0
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,0,0,0], [[0,0,0]]),
        ([], []),
        ([1,-1,-1,0], [[-1,0,1]]),
    ]
    for arr, expected in tests:
        out = sol.threeSum(arr.copy())
        # convert to sets of tuples for order-insensitive comparison
        out_set = {tuple(x) for x in out}
        exp_set = {tuple(x) for x in expected}
        print(f"{arr} -> {out} (expected {expected})")
        assert out_set == exp_set
    print("All tests passed.")
