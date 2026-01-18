"""
LeetCode: 3205. Maximum Profit from Trading Stocks with Strategy (Medium)
Problem Link: https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-strategy/
Author: Aditya Pandey
Date: 16-01-2026

--------------------------------------------------
Problem:
You are given:
- prices[i]: price of a stock on day i
- strategy[i]: 0 or 1 indicating whether you hold stock on day i
- k: length of a subarray where strategy can be flipped optimally

Goal:
Maximize total profit after applying at most one modification
on a subarray of length k.

--------------------------------------------------
Pattern:
Sliding Window + Prefix Optimization

--------------------------------------------------
Approach:
1. Compute the base profit using the given strategy:
       base = Σ(prices[i] * strategy[i])

2. Split the k-window into two halves:
   - First half: losing contribution (remove strategy effect)
   - Second half: gaining contribution (force buy → sell)

3. Use a sliding window to:
   - Maintain contribution of first half (first_h)
   - Maintain contribution of second half (sec_h)
   - Track maximum extra gain achievable

4. Final answer:
       base + max(0, best_gain)

--------------------------------------------------
Why it Works:
- Fixed-size sliding window ensures O(n) scan
- Separating window halves allows constant-time updates
- Avoids recomputation of full subarray effects

--------------------------------------------------
Time Complexity:
O(n)

Space Complexity:
O(1)

--------------------------------------------------
Things to Pay Attention:
- Correct index movement in sliding window
- Half window handling (k // 2)
- Avoid negative profit by using max(0, gain)
--------------------------------------------------
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        half = k // 2

        # Base profit using original strategy
        base = sum(p * s for p, s in zip(prices, strategy))

        first_h = 0
        second_h = 0

        # Initial window setup
        for i in range(half):
            first_h -= strategy[i] * prices[i]

        for i in range(half, k):
            second_h += prices[i] - strategy[i] * prices[i]

        gain = first_h + second_h

        # Sliding window
        for s in range(1, len(prices) - k + 1):
            out_first = s - 1
            in_first = s + half - 1

            out_second = s + half - 1
            in_second = s + k - 1

            first_h += strategy[out_first] * prices[out_first]
            first_h -= strategy[in_first] * prices[in_first]

            second_h -= prices[out_second] - strategy[out_second] * prices[out_second]
            second_h += prices[in_second] - strategy[in_second] * prices[in_second]

            gain = max(gain, first_h + second_h)

        return base + max(0, gain)


# -----------------------
# Local Testing
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1, 3, 2, 4], [1, 0, 1, 0], 2))
