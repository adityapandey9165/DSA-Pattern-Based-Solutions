"""
LeetCode: 696. Count Binary Substrings (Easy)
Problem Link: https://leetcode.com/problems/count-binary-substrings/
Author: Aditya Pandey
Date: 2026-02-19

Problem:
Given a binary string s, return the number of non-empty substrings that have the
same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
(Example: "0011", "01" are valid; "0101" is not.)

------------------------------------------------------------
Pattern:
Greedy / Group Counting (Adjacent group lengths)

------------------------------------------------------------
Intuition (how it works):
- Any valid substring must consist of a block of consecutive identical chars
  followed immediately by a block of the opposite char (e.g., "000111").
- For two adjacent groups of lengths `a` and `b`, they contribute `min(a, b)`
  valid substrings (for each possible length `1..min(a,b)` we can take that many
  chars from each side).

So we only need to scan the string once, count consecutive groups, and sum
`min(previous_group_length, current_group_length)`.

This yields an O(n) time, O(1) space solution.

------------------------------------------------------------
Algorithm (one pass):
1. Maintain `prev` = length of previous group, `cur` = length of current group.
2. Initialize `cur = 1`, `prev = 0`, `res = 0`.
3. Iterate s from index 1 to end:
   - If s[i] == s[i-1]: `cur += 1`
   - Else:
       - `res += min(prev, cur)`
       - `prev = cur`
       - `cur = 1`
4. After loop, add `min(prev, cur)` for the last boundary.
5. Return `res + min(prev, cur)`.

------------------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(1)

------------------------------------------------------------
Common pitfalls:
- Forgetting to add `min(prev, cur)` after the loop (final group pairing).
- Off-by-one bugs when initializing `cur` and iterating from index 1.
- Using substring checks (O(n^2)) — avoid explicit substring scanning.
- Not handling short strings correctly (length < 2 → 0).

------------------------------------------------------------
Code (optimal, one-pass)
"""
from typing import List


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0

        cur = 1        # length of current consecutive group
        prev = 0       # length of previous consecutive group
        res = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(cur, prev)
                prev = cur
                cur = 1

        # add contribution of last boundary
        res += min(prev, cur)
        return res


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("00110011", 6),   # ["0011","01","1100","10","0011","01"]
        ("10101", 4),      # ["10","01","10","01"]
        ("00110", 3),      # ["0011","01","10"]
        ("0", 0),
        ("01", 1),
        ("001", 1),
    ]
    for s, expected in tests:
        out = sol.countBinarySubstrings(s)
        print(f"{s!r} -> {out} (expected: {expected})")
