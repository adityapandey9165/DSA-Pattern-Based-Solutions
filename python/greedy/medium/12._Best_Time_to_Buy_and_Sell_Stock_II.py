"""
LeetCode: 122. Best Time to Buy and Sell Stock II (Medium)
Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Author: Aditya Pandey
Date: 2025-09-05

Problem:
Given an array `prices` where prices[i] is the price of a given stock on day i,
you may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Return the maximum profit you can achieve.
Note: You may not engage in multiple transactions simultaneously (you must sell before you buy again).

Pattern: Greedy — Sum of Positive Differences (Peak-Valley)

Approach:
- Any time the price goes up from day i-1 to day i, capturing that increase (buy at i-1, sell at i) is beneficial.
- The optimal total profit equals the sum of all positive increases between consecutive days:
    profit = sum(max(0, prices[i] - prices[i-1]) for i in 1..n-1)
- This is equivalent to repeatedly buying at local minima and selling at local maxima, but simpler to implement.

Time Complexity: O(n) — single pass through prices.
Space Complexity: O(1) — constant extra space.

Common Mistakes:
- Trying to track explicit buy/sell days with complicated logic (unnecessary).
- Using nested loops to find all pairs (O(n^2)).
- Forgetting the constraint that you must sell before buying again.

Example Walkthrough:
prices = [7,1,5,3,6,4]
- Day 2: 1->5: add 4
- Day 4: 3->6: add 3
Total profit = 4 + 3 = 7

prices = [1,2,3,4,5]
- Add (2-1)+(3-2)+(4-3)+(5-4) = 4 (buy day1 sell day5 equivalently)

"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Greedy: sum positive differences between consecutive days.
        """
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff
        return profit


if __name__ == "__main__":
    # quick tests for revision
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))     # expected 7
    print(sol.maxProfit([1, 2, 3, 4, 5]))        # expected 4
    print(sol.maxProfit([7, 6, 4, 3, 1]))        # expected 0
    print(sol.maxProfit([1, 2, 3, 0, 2]))        # expected 3
