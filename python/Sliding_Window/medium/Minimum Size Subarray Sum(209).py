"""
LeetCode: 209. Minimum Size Subarray Sum (Medium)
Problem link: https://leetcode.com/problems/minimum-size-subarray-sum/
Author: Aditya Pandey
Date: 2025-09-24

Problem:
Given an array of positive integers `nums` and a positive integer `target`, 
return the minimal length of a contiguous subarray of which the sum is at least `target`. 
If there is no such subarray, return 0.

Pattern: Sliding window / two pointers (variable-length window)

Approach (intuition):
- Use two pointers `l` and `r` to maintain a sliding window `nums[l..r]` and a running sum `s`.
- Expand `r` to grow the window until `s >= target`.
- When `s >= target`, try to shrink the window from the left (`l += 1`) while maintaining `s >= target` to find the minimal window for this `r`.
- Keep track of the smallest window length seen.
- Return 0 if no valid window was found.

Time Complexity: O(n) — each index is visited at most twice (once by r and once by l).
Space Complexity: O(1) — constant extra space.

Common Mistakes:
- Using nested loops that lead to O(n^2).
- Forgetting to handle the case where no subarray meets the target → must return 0.
- Off-by-one errors when computing window length (use r - l + 1).
- Using `sum(nums)` as a pre-check costs O(n) extra and is unnecessary — the sliding window will detect impossibility without it.

"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Sliding-window implementation (O(n) time).
        Uses res = n+1 as sentinel for "not found".
        """
        n = len(nums)
        l = 0
        s = 0
        res = n + 1  # sentinel: if unchanged, means no valid subarray found

        for r in range(n):
            s += nums[r]
            # shrink from left while window sum >= target
            while l <= r and s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1

        return 0 if res == n + 1 else res


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    tests = [
        (7, [2,3,1,2,4,3], 2),   # [4,3] or [3,4] etc.
        (4, [1,4,4], 1),
        (11, [1,2,3,4,5], 3),    # [3,4,5]
        (15, [1,2,3,4,5], 5),    # whole array
        (100, [1,2,3], 0),       # impossible
        (3, [1,1,1,1,1,1,1,1], 3),
    ]

    for target, nums, expected in tests:
        out = sol.minSubArrayLen(target, nums.copy())
        print(f"target={target}, nums={nums} -> {out} (expected={expected})")
        assert out == expected
    print("All tests passed.")
