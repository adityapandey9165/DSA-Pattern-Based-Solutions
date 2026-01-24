"""
LeetCode: 1877. Minimize Maximum Pair Sum in Array (Medium)
Problem Link: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
Author: Aditya Pandey
Date: 2026-01-19

--------------------------------------------------
Problem:
Given an array `nums` of even length, pair up the elements such that
the maximum pair sum is minimized.

Return the minimized maximum pair sum.

--------------------------------------------------
Pattern:
Greedy + Counting Sort / Two Pointers

--------------------------------------------------
Approach:
To minimize the maximum pair sum:
- Always pair the smallest available number with the largest available number.

Instead of sorting (O(n log n)), we use **frequency counting**
because the constraints allow values up to 10^5.

Steps:
1. Build a frequency array `freq` where freq[x] = count of x in nums.
2. Use two pointers:
   - `l` starting from smallest value
   - `r` starting from largest value
3. Repeatedly:
   - Move `l` to next available number
   - Move `r` to next available number
   - Pair (l, r)
   - Track the maximum sum
4. Continue until all elements are paired.

--------------------------------------------------
Why This Works:
- Pairing smallest with largest minimizes worst-case pair sum
- Frequency array avoids full sorting
- Two-pointer greedy guarantees optimal pairing

--------------------------------------------------
Example:
nums = [3,5,2,3]
Pairs: (2,5), (3,3)
Maximum pair sum = 7

--------------------------------------------------
Time Complexity:
O(n + K), where K = max value (10^5)

Space Complexity:
O(K)

--------------------------------------------------
Things to Pay Attention:
- Skip values with zero frequency
- Update frequency after each pairing
- Ensure pointers do not cross
--------------------------------------------------
"""

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        K = 10**5
        freq = [0] * (K + 1)

        # Count frequency
        for num in nums:
            freq[num] += 1

        l, r = 0, K
        res = 0

        # Two-pointer pairing using frequency array
        while l <= r:
            while l <= r and freq[l] == 0:
                l += 1
            while l <= r and freq[r] == 0:
                r -= 1
            if l > r:
                break

            res = max(res, l + r)
            freq[l] -= 1
            freq[r] -= 1

        return res


# -----------------------
# Local Testing
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.minPairSum([3, 5, 2, 3]))     # Expected: 7
    print(sol.minPairSum([3, 5, 4, 2, 4, 6]))  # Expected: 8
