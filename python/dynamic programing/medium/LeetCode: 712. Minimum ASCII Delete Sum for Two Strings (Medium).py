"""
LeetCode: 712. Minimum ASCII Delete Sum for Two Strings (Medium)
Problem Link: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
Author: Aditya Pandey
Date: 16-01-2026

--------------------------------------------------
Problem:
Given two strings s1 and s2, return the minimum ASCII sum of deleted characters
to make the two strings equal.

You can delete characters from either string.

--------------------------------------------------
Pattern:
Dynamic Programming – String DP (LCS Variant)

--------------------------------------------------
Approach:
This problem is a variation of **Longest Common Subsequence (LCS)**.

Instead of maximizing the common subsequence,
we minimize the ASCII cost of deleted characters.

We use **Top-Down DP (Memoization)**:

Define:
    sol(i, j) → minimum delete sum to make
                s1[i:] and s2[j:] equal

Cases:
1. If one string is exhausted:
   - Delete all remaining characters of the other string.

2. If characters match:
   - No deletion needed, move both pointers.

3. If characters differ:
   - Option 1: Delete s1[i]
   - Option 2: Delete s2[j]
   - Take the minimum cost.

Memoization avoids recomputation.

--------------------------------------------------
Time Complexity:
O(n × m)

Space Complexity:
O(n × m)  (memo table + recursion stack)

--------------------------------------------------
Things to Pay Attention:
- Base cases when one string finishes
- Use ASCII value via ord()
- This is NOT classical LCS length DP, but cost-based DP
--------------------------------------------------
"""

from typing import *
from functools import lru_cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}

        def sol(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            # If s1 is exhausted, delete remaining s2 chars
            if i == len(s1):
                return sum(ord(c) for c in s2[j:])

            # If s2 is exhausted, delete remaining s1 chars
            if j == len(s2):
                return sum(ord(c) for c in s1[i:])

            # Characters match → no deletion
            if s1[i] == s2[j]:
                memo[(i, j)] = sol(i + 1, j + 1)
            else:
                delete_s1 = ord(s1[i]) + sol(i + 1, j)
                delete_s2 = ord(s2[j]) + sol(i, j + 1)
                memo[(i, j)] = min(delete_s1, delete_s2)

            return memo[(i, j)]

        return sol(0, 0)


# -----------------------
# Local Testing
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.minimumDeleteSum("sea", "eat"))   # Expected: 231
    print(sol.minimumDeleteSum("delete", "leet"))  # Expected: 403
