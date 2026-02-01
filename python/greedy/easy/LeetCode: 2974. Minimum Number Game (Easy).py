"""
LeetCode: 2974. Minimum Number Game (Easy)
Problem Link: https://leetcode.com/problems/minimum-number-game/
Author: Aditya Pandey
Date: 2026-01-19

--------------------------------------------------
Problem:
Given an array `nums`, compute the minimum possible cost defined as:
- Take nums[0]
- Add the two smallest values from the remaining elements

Return the total cost.

--------------------------------------------------
Pattern:
Greedy / Array Scan

--------------------------------------------------
Approach:
1. The first element nums[0] must always be included in the cost.
2. From the remaining elements (nums[1:]), find the two smallest numbers.
3. Add nums[0] + smallest + second_smallest.

Instead of sorting the array (O(n log n)),
we scan once and keep track of the two minimum values.

--------------------------------------------------
Why This Works:
- Only the two smallest elements after index 0 matter.
- Greedy choice of smallest values guarantees minimum sum.
- Single pass keeps the solution optimal and efficient.

--------------------------------------------------
Time Complexity:
O(n)

Space Complexity:
O(1)

--------------------------------------------------
Things People Commonly Miss:
1. nums[0] is mandatory — do NOT include it in min comparisons.
2. Avoid sorting; it’s unnecessary and slower.
3. Carefully update first and second minimums.
--------------------------------------------------
"""

from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)

        # nums[0] must be included
        res = nums[0]

        # Find two smallest values from nums[1:]
        first_min = float('inf')
        second_min = float('inf')

        for val in nums[1:]:
            if val < first_min:
                second_min = first_min
                first_min = val
            elif val < second_min:
                second_min = val

        return res + first_min + second_min


# -----------------------
# Local Testing
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumCost([1, 2, 3, 4]))    # Expected: 6
    print(sol.minimumCost([5, 4, 3]))       # Expected: 12
