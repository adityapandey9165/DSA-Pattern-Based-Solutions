"""
LeetCode: 121. Best Time to Buy and Sell Stock (Easy)
Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Author: Aditya Pandey
Date: 2025-09-04

Problem:
You are given an array `prices` where prices[i] is the stock price on the i-th day.
You want to maximize profit by choosing one day to buy and a different future day to sell.
Return the maximum profit you can achieve. If no profit is possible, return 0.

Pattern: Greedy — Track Minimum Price and Maximum Profit

Approach:
- Track the minimum price seen so far (`m`).
- At each day’s price:
  • Compute profit = price - m.
  • Update result `res` if profit is greater.
  • Update `m` if current price is lower.
- Return `res` as maximum profit.

Time Complexity: O(n) — single pass
Space Complexity: O(1) — constant space

Common Mistakes:
- Allowing sell before buy (must always buy first).
- Returning negative profits instead of 0.
- Using O(n^2) brute force by checking all pairs.

Example Walkthrough:
prices = [7,1,5,3,6,4]
m=7, res=0
Day 1: 7 -> profit=0 -> res=0
Day 2: 1 -> new min=1
Day 3: 5 -> profit=4 -> res=4
Day 4: 3 -> profit=2 -> res=4
Day 5: 6 -> profit=5 -> res=5
Day 6: 4 -> profit=3 -> res=5
Result = 5
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Return the maximum profit from one buy-sell transaction.
        """
        m = prices[0]   # minimum price seen so far
        res = 0         # maximum profit

        for price in prices:
            if price - m > res:
                res = price - m
            if price < m:
                m = price

        return res


if __name__ == "__main__":
    # Quick tests for practice
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # expected 5
    print(sol.maxProfit([7, 6, 4, 3, 1]))     # expected 0
    print(sol.maxProfit([1, 2, 3, 4, 5]))     # expected 4
