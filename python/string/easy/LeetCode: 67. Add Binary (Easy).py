"""
LeetCode: 67. Add Binary (Easy)
Problem Link: https://leetcode.com/problems/add-binary/
Author: Aditya Pandey
Date: 2026-02-15

Problem:
Given two binary strings a and b, return their sum as a binary string.

Example:
a = "11", b = "1" -> "100"

------------------------------------------------------------
Pattern:
String Simulation / Two Pointers + Carry (Elementary Math on strings)

------------------------------------------------------------
Approach (how it works):
- Use two pointers i, j starting from the end of strings a and b.
- Maintain an integer carry (0 or 1).
- Repeatedly add digits a[i] and b[j] (if present) plus carry.
- Append (total % 2) to result, update carry = total // 2.
- Continue while any pointer is valid or carry != 0.
- Reverse the collected digits to form the final binary string.

This simulates manual binary addition (right-to-left), and works for strings of different lengths.

------------------------------------------------------------
Why this is good:
- O(max(len(a), len(b))) time — linear in input length.
- O(1) extra space except for output (res buffer).
- No large-number conversions required (safe for very long strings).

------------------------------------------------------------
Time Complexity: O(n) where n = max(len(a), len(b))
Space Complexity: O(n) for output string

------------------------------------------------------------
Common pitfalls:
- Forgetting to process final carry (e.g., when both strings exhausted).
- Using int(a,2)+int(b,2) for very long strings may overflow or be slow in some languages.
- Off-by-one with indices — loop condition should allow carry to drive another digit.
- Remember to reverse the result at the end (we build digits LSB→MSB).

------------------------------------------------------------
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = []

        # Process from LSB to MSB
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            # current bit and new carry
            res.append(str(total % 2))
            carry = total // 2

        # reverse to get MSB -> LSB order
        return "".join(reversed(res))


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("0", "0", "0"),
        ("1", "111", "1000"),
        ("1111", "1", "10000"),
        ("101", "0", "101"),
    ]

    for a, b, expected in tests:
        out = sol.addBinary(a, b)
        print(f"{a} + {b} -> {out} (expected: {expected})")

