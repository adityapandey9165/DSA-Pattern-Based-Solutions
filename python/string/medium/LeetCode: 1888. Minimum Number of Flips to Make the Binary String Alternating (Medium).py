"""
LeetCode: 1888. Minimum Number of Flips to Make the Binary String Alternating (Medium)
Problem Link: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
Author: Aditya Pandey
Date: 2026-03-07

Problem:
Given a binary string s, you may perform any number of shifts (move first char to end).
Return the minimum number of flips (change '0'->'1' or '1'->'0') needed to make
the string alternating (either "0101..." or "1010...") after any number of shifts.

Key observation:
Shifting is equivalent to choosing any rotation of s. To consider all rotations
efficiently, concatenate s with itself (s+s) and slide a window of length n.
For each window (rotation), compute flips needed to match the two alternating targets.

Pattern:
Sliding Window + String Doubling (rotation enumeration) + Greedy mismatch counting

Why this works:
- There are only two alternating targets for a given length n:
    patternA = "0101..."
    patternB = "1010..."
- For any rotation, the minimal flips is min(mismatches to patternA, mismatches to patternB).
- Doubling s and sliding a window of size n enumerates every rotation exactly once.
- Maintain mismatch counts incrementally (add right char, remove left char) → O(1) per step.

Time Complexity: O(n) (we process 2n chars but window length n → linear)
Space Complexity: O(1) extra (excluding input)

Common pitfalls:
- Forgetting to double the string (missing rotations).
- Off-by-one window management (when removing left char).
- Not updating both pattern mismatch counters correctly.
- Using string slicing inside the hot loop (avoid it — update counters directly).

------------------------------------------------------------
Implementation (clean, readable)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        # Double the string to cover all rotations
        ss = s + s

        # We'll count mismatches for two patterns:
        # pattern1 (starting with '0'): index even -> '0', odd -> '1'
        # pattern2 (starting with '1'): index even -> '1', odd -> '0'
        diff1 = 0  # mismatches vs pattern1 in current window
        diff2 = 0  # mismatches vs pattern2 in current window

        res = n  # max flips never exceeds n
        l = 0

        for r in range(2 * n):
            ch = ss[r]
            # expected for pattern1 at index r: '0' if r%2==0 else '1'
            if ch != ('0' if r % 2 == 0 else '1'):
                diff1 += 1
            # expected for pattern2 at index r: '1' if r%2==0 else '0'
            if ch != ('1' if r % 2 == 0 else '0'):
                diff2 += 1

            # Once window exceeds size n, remove left char contribution and slide
            if r - l + 1 > n:
                left_ch = ss[l]
                if left_ch != ('0' if l % 2 == 0 else '1'):
                    diff1 -= 1
                if left_ch != ('1' if l % 2 == 0 else '0'):
                    diff2 -= 1
                l += 1

            # When window has size exactly n, consider its cost
            if r - l + 1 == n:
                res = min(res, diff1, diff2)

        return res


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("111000", 2),
        ("010", 0),
        ("1110", 1),
        ("0000", 2),
        ("10", 0),
        ("01", 0),
        ("1", 0),
    ]
    for s, expected in tests:
        out = sol.minFlips(s)
        print(f"{s!r} -> {out} (expected: {expected})")
    
