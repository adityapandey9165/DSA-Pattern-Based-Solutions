"""
LeetCode: 238. Product of Array Except Self (Medium)
Problem link: https://leetcode.com/problems/product-of-array-except-self/
Author: Aditya Pandey
Date: 2025-09-12

Problem:
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to
the product of all the elements of nums except nums[i].

You must write an algorithm that runs in O(n) time and without using the division operation.
The product of elements will fit in a 32-bit integer (assumption for typical LeetCode).

Pattern: Prefix & Suffix Products (Two-pass, space-optimized)

Approach (Prefix-Suffix, O(n) time, O(1) extra space):
- The idea is to compute for each index i:
    answer[i] = product of elements to the left of i  *  product of elements to the right of i
- Do two passes:
  1. Left-to-right pass: build prefix products and store them in answer[].
     - Maintain `prefix` variable. For each i: answer[i] = prefix; prefix *= nums[i]
  2. Right-to-left pass: maintain `suffix` variable and multiply answer[i] by suffix.
     - For i from n-1 down to 0: answer[i] *= suffix; suffix *= nums[i]
- This yields the final array without using division. Using only the output array plus two scalars gives O(1) extra space (ignoring output).

Time Complexity: O(n) — two linear passes.
Space Complexity: O(1) extra space (output array not counted per problem statement).

Why not use division?
- Division fails when zeros appear and is generally not allowed by the problem constraints.
- Division-based approach would need special handling of zero counts and is less robust.

Common Mistakes:
- Using division without handling zeros (wrong when zeros present).
- Building two full arrays for prefix and suffix unnecessarily (uses O(n) extra space).
- Off-by-one when calculating prefix/suffix indices.
- Forgetting to treat `answer[i]` as the prefix product before updating prefix.

Example Walkthrough:
nums = [1, 2, 3, 4]
n = 4

Initialize:
res = [1, 1, 1, 1]
prefix = 1

Left-to-right (prefix):
i=0: res[0] = prefix = 1; prefix *= nums[0] -> prefix = 1
i=1: res[1] = prefix = 1; prefix *= nums[1] -> prefix = 2
i=2: res[2] = prefix = 2; prefix *= nums[2] -> prefix = 6
i=3: res[3] = prefix = 6; prefix *= nums[3] -> prefix = 24

After prefix pass: res = [1, 1, 2, 6]

Right-to-left (suffix):
suffix = 1
i=3: res[3] *= suffix -> 6 * 1 = 6; suffix *= nums[3] -> suffix = 4
i=2: res[2] *= suffix -> 2 * 4 = 8; suffix *= nums[2] -> suffix = 12
i=1: res[1] *= suffix -> 1 * 12 = 12; suffix *= nums[1] -> suffix = 24
i=0: res[0] *= suffix -> 1 * 24 = 24; suffix *= nums[0] -> suffix = 24

Final res = [24, 12, 8, 6]

Interview follow-up / common questions:
- Can you do it without using extra arrays? (Yes — prefix/suffix in-place into output array.)
- What if the numbers are large — how to avoid overflow? (Use 64-bit integers or modulo arithmetic as required.)
- How to handle when the product must be reported modulo M (e.g., 1e9+7)? (Use modular multiplication; be careful with zeros.)
- How to handle zeros quickly? (Count zeros; if more than one zero, all outputs are 0; if exactly one zero, only the index of zero gets product of others.)
- Can you do this in parallel? (Yes — prefix/suffix scans are parallelizable / reduce-friendly.)
- What changes if you are given a stream of numbers? (You need different approach; exact answers require two passes so you’d need buffering or multiple passes over stored data.)
- Could you generalize to compute product excluding a sliding window? (Yes — techniques with prefix/suffix or segment trees can help.)
- What's the difference between prefix/suffix technique and using logarithms to convert multiplication into addition? (Logs avoid overflow but cause precision issues and cannot handle zeros directly.)

"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Compute product of array except self using prefix & suffix products.
        """
        n = len(nums)
        # result array initialized to 1s
        res = [1] * n

        # prefix pass: res[i] stores product of all elements to the left of i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # suffix pass: multiply res[i] by product of all elements to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([0, 0], [0, 0]),
        ([0, 4, 0], [0, 0, 0]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
        ([1], [1]),
    ]

    for nums, expected in tests:
        out = sol.productExceptSelf(nums.copy())
        print(f"nums={nums} -> result={out} (expected={expected})")
