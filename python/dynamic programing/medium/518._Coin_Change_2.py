"""
LeetCode: 518. Coin Change 2 (Medium)
Problem link: https://leetcode.com/problems/coin-change-2/
Author: Aditya Pandey
Date: 2025-09-07

Problem:
Given an integer array `coins` of distinct coin denominations and an integer `amount`,
return the number of combinations that make up that amount. You may use an infinite number
of each coin. The order of coins in combinations does not matter (combinations, not permutations).

This file contains two approaches:
1) Top-down DFS with memoization (easy to write and explain)  -> change_memo (uses lru_cache)
2) Bottom-up dynamic programming (standard optimal)         -> change (default)

Which to use in interviews?
- **Explain the DP idea** (dp[x] = number of ways to make x). Interviewers like the DP recurrence and the reason we iterate coins first.
- **Implement whichever you can write clearly**: top-down memo is fine if you explain states and complexity. However, many interviewers prefer or expect the bottom-up DP for this classical problem because it's concise and explicitly O(amount * len(coins)).
"""

from typing import List
from functools import lru_cache


class Solution:
    # -------------------------
    # Approach 1: Top-down DFS + Memo (readable, explainable)
    # -------------------------
    def change_memo(self, amount: int, coins: List[int]) -> int:
        """
        Top-down recursion with memoization.
        State: (i, total) where i is current coin index and total is current sum.
        dfs(i, total) = number of ways to reach `amount` using coins[i:].
        """
        if amount == 0:
            return 1

        coins = sorted(coins)  # sort for determinism (not required)
        
        @lru_cache(maxsize=None)
        def dfs(i: int, total: int) -> int:
            # base cases
            if total == amount:
                return 1
            if total > amount or i == len(coins):
                return 0

            # two choices:
            # 1) take current coin (stay at i since unlimited supply)
            take = dfs(i, total + coins[i])
            # 2) skip current coin -> move to next coin
            skip = dfs(i + 1, total)

            return take + skip

        return dfs(0, 0)

    # -------------------------
    # Approach 2: Bottom-up DP (recommended default)
    # -------------------------
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Bottom-up DP (combinations count).
        dp[x] = number of ways to make amount x using processed coins.
        Iterate coins first to ensure combinations are counted (order doesn't matter).
        """
        # base dp
        dp = [0] * (amount + 1)
        dp[0] = 1  # one way to make 0: pick nothing

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]


# ---------- Quick tests ----------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        (5, [1, 2, 5], 4),     # {5}, {2+2+1}, {2+1+1+1}, {1x5}
        (3, [2], 0),           # cannot make 3 with coin 2
        (10, [10], 1),         # only [10]
        (0, [1, 2, 3], 1),     # amount 0 -> one way (empty set)
        (5, [2, 3, 5], 2),     # {2+3}, {5}
    ]

    for amount, coins, expected in tests:
        out_dp = sol.change(amount, coins)
        out_memo = sol.change_memo(amount, coins)
        print(f"amount={amount}, coins={coins}  -> dp={out_dp}, memo={out_memo} (expected={expected})")
