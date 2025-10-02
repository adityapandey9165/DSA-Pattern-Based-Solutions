"""
LeetCode: 76. Minimum Window Substring (Hard)
Problem link: https://leetcode.com/problems/minimum-window-substring/
Author: Aditya Pandey
Date: 2025-10-02

Problem:
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t 
(including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

Pattern: Sliding Window (two pointers + hashmap)

Approach:
1. Use two dictionaries (or Counters):
   - t_count: frequency of chars in t
   - window: frequency of chars in current window [l..r] of s
2. Expand right pointer `r` → add chars to window
3. If all required chars are satisfied (`matches == len(t_count)`), shrink left pointer `l`
   to minimize window while still satisfying condition.
4. Track minimum window length and result substring.
"""

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Count characters in t
        t_count = Counter(t)
        window = defaultdict(int)

        l = 0
        matches = 0
        min_len = float("inf")
        res = ""

        for r in range(len(s)):
            # Expand window
            window[s[r]] += 1
            if window[s[r]] == t_count[s[r]]:
                matches += 1

            # Contract window while valid
            while matches == len(t_count):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l : r + 1]

                window[s[l]] -= 1
                if window[s[l]] < t_count[s[l]]:
                    matches -= 1
                l += 1

        return res


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
    print(sol.minWindow("a", "a"))                # "a"
    print(sol.minWindow("a", "aa"))               # ""
    print(sol.minWindow("ab", "b"))               # "b"
    print(sol.minWindow("aa", "aa"))              # "aa"
