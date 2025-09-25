"""
LeetCode: 167. Two Sum II - Input Array Is Sorted (Easy)
Problem link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Author: Aditya Pandey
Date: 2025-09-23

Problem:
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific `target` number.
Return the indices of the two numbers (index1, index2) as a list [i, j] of length 2,
where 1 <= i < j <= numbers.length.
You may assume each input has exactly one solution and you may not use the same element twice.

Pattern: Two Pointers (left/right) — O(n) time, O(1) extra space

Approach:
- Use two pointers `l` (start) and `r` (end).
- Compute `cur = numbers[l] + numbers[r]`.
  - If `cur < target`: move left pointer right (l += 1) to increase sum.
  - If `cur > target`: move right pointer left (r -= 1) to decrease sum.
  - If equal: return [l+1, r+1] (convert to 1-based indices).
- Because the array is sorted, this greedy two-pointer scan always finds the answer in one pass.

Time Complexity: O(n) — each pointer moves at most n steps  
Space Complexity: O(1) — constant extra space

Common Mistakes:
- Returning 0-based indices (problem asks for 1-based).
- Returning a tuple instead of a list (LeetCode expects list).
- Using a hash map unnecessarily (works, but O(n) extra space; two-pointer is simpler here).
- Not handling edge cases like very small arrays (but constraints guarantee solution exists).

Interview follow-ups:
- What if the array is not sorted? (Use hash map -> O(n) time, O(n) space.)
- What if you need to support multiple queries with the same array? (Precompute hashmap of complements or use two-pointer on each query.)
- Can you do it in-place/constant space? (Yes — this two-pointer solution.)

"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two-pointer solution returning 1-based indices [i, j].
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            cur = numbers[l] + numbers[r]
            if cur < target:
                l += 1
            elif cur > target:
                r -= 1
            else:
                # Problem requires 1-based indices
                return [l + 1, r + 1]
        # per problem constraints, there is exactly one solution;
        # return [-1, -1] defensively (should never happen on valid input)
        return [-1, -1]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,7,11,15], 9, [1,2]),
        ([2,3,4], 6, [1,3]),
        ([-1,0], -1, [1,2]),
        ([5,25,75], 100, [2,3]),
    ]
    for nums, target, expected in tests:
        out = sol.twoSum(nums, target)
        print(f"numbers={nums}, target={target} -> {out} (expected={expected})")
        assert out == expected
    print("All tests passed.")
