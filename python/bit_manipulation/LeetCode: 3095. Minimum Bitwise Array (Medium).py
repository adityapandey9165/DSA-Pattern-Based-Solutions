"""
LeetCode: 3095. Minimum Bitwise Array (Medium)
Problem Link: https://leetcode.com/problems/minimum-bitwise-array/
Author: Aditya Pandey
Date: 2026-01-19

--------------------------------------------------
Problem:
You are given an array `nums`. For each element nums[i], find the minimum integer `x`
such that:

    x OR (x + 1) == nums[i]

If no such x exists, return -1 for that element.

--------------------------------------------------
Pattern:
Bit Manipulation

--------------------------------------------------
Key Observations:
1. If nums[i] is EVEN:
   - It is impossible to represent it as x | (x + 1)
   - Reason: x | (x + 1) is always ODD
   → Answer is -1

2. If nums[i] is ODD:
   - A valid x always exists.

--------------------------------------------------
Bitwise Insight:
For an odd number `n`:
- Count the number of **continuous trailing 1s** in binary.
- Let this count be `k`.

Example:
n = 23 → binary: 10111
Trailing 1s = 3

The smallest valid x is obtained by:
- Turning the **highest trailing 1** into 0
- Keeping all higher bits unchanged

Formula:
    x = n - 2^(k - 1)

--------------------------------------------------
Why This Works:
- Subtracting 2^(k-1) clears exactly one trailing 1
- This ensures:
      x | (x + 1) = n
- Using the highest trailing 1 gives the **minimum x**

--------------------------------------------------
Examples:
n = 7   (111)   → k = 3 → x = 7 - 4 = 3
n = 23  (10111) → k = 3 → x = 23 - 4 = 19
n = 10  (1010)  → even → -1

--------------------------------------------------
Time Complexity:
O(n * log(max(nums)))

Space Complexity:
O(1) extra space (excluding output)

--------------------------------------------------
Things to Pay Attention:
- Trailing 1s count
- Even numbers immediately return -1
- Bitwise shifts are faster than string conversion
--------------------------------------------------
"""

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            # Even numbers cannot be formed
            if n % 2 == 0:
                ans.append(-1)
                continue

            # Count trailing 1s
            k = 0
            t = n
            while t & 1:
                k += 1
                t >>= 1

            # Remove the highest trailing 1
            ans.append(n - (1 << (k - 1)))

        return ans


# -----------------------
# Local Testing
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.minBitwiseArray([2, 3, 5, 7, 23]))
    # Expected: [-1, 1, 4, 3, 19]
