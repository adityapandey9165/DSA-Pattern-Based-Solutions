"""
LeetCode: 3761. Minimum Absolute Distance Between Mirror Pairs (Medium)
Author: Aditya Pandey
Date: 2026-04-06

------------------------------------------------------------
Problem:
Given an array of integers nums, find the minimum distance
between two indices i and j such that:

nums[i] is the reverse of nums[j]

Return the minimum absolute difference |i - j|.
If no such pair exists, return -1.

------------------------------------------------------------
Example:
nums = [12, 21, 34, 43]

Pairs:
12 ↔ 21 → distance = 1
34 ↔ 43 → distance = 1

Answer = 1

------------------------------------------------------------
Pattern:
HashMap + Reverse Matching

------------------------------------------------------------
Approach:
1. Traverse the array once
2. Maintain a hashmap:
   last[value] = last index where value (or reversed value) is seen

3. For each number:
   - If current value exists in hashmap → we found a reverse pair
   - Update minimum distance
   - Store reverse(value) in hashmap for future matches

------------------------------------------------------------
Key Idea:
Instead of checking reverse every time,
we PRE-STORE reversed values.

So future numbers can match instantly in O(1).

------------------------------------------------------------
Why this works:
Example:
nums = [12, 21]

Step 1:
Store reverse(12) → 21 at index 0

Step 2:
When 21 appears → found match in hashmap

------------------------------------------------------------
Time Complexity:
O(n * d)

n = number of elements
d = digits in number (for reverse operation)

------------------------------------------------------------
Space Complexity:
O(n)

------------------------------------------------------------
Things to Pay Attention To:
- Reverse using string or math
- Store reverse(value), not original
- Always check before updating map
- Handle no-pair case

------------------------------------------------------------
Edge Cases:
- No mirror pairs → return -1
- Single element → return -1
- Leading zeros after reverse (e.g., 10 → 01 → 1)

------------------------------------------------------------
Common Mistakes:
- Storing original instead of reverse
- Updating hashmap before checking
- Ignoring leading zero cases
------------------------------------------------------------
"""

from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        def reverse(a: int) -> int:
            return int(str(a)[::-1])

        last = {}
        res = float('inf')

        for i, val in enumerate(nums):

            # check if this value was expected (as reverse)
            if val in last:
                res = min(res, i - last[val])

            # store reverse for future matching
            rev = reverse(val)
            last[rev] = i

        return res if res != float('inf') else -1


# -----------------------
# Quick tests
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.minMirrorPairDistance([12, 21, 34, 43]))  # Expected: 1
    print(sol.minMirrorPairDistance([10, 1, 100]))      # Expected: 1
    print(sol.minMirrorPairDistance([1, 2, 3]))         # Expected: -1
