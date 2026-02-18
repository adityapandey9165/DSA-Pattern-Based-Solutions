"""
LeetCode: 693. Binary Number with Alternating Bits (Easy)
Problem Link: https://leetcode.com/problems/binary-number-with-alternating-bits/
Author: Aditya Pandey
Date: 2026-02-16

Problem:
Given a positive integer n, return True if the binary representation of n
has alternating bits: that is, no two adjacent bits are the same (e.g. 1010...),
otherwise return False.

Example:
Input: 5  (binary 101)  -> True
Input: 7  (binary 111)  -> False

------------------------------------------------------------
Pattern:
Bit manipulation (bit-trick) — constant-time checks using XOR and power-of-two test.

------------------------------------------------------------
Optimal Idea (bit-trick) — O(1) time:
1. If n has alternating bits, shifting it by 1 and XORing will produce a sequence
   of consecutive 1s. Example:
     n =  1 0 1 0  (binary)
    n>>1 = 0 1 0 1
    n ^ (n>>1) = 1 1 1 1   (a block of ones)

2. A number x that is a contiguous string of 1s (like 0b111...111) satisfies:
       x & (x + 1) == 0
   because x+1 is a power of two and has exactly one bit set which does not overlap with x.

So combine both steps:
    x = n ^ (n >> 1)
    return (x & (x + 1)) == 0

This is a tiny constant-time solution (few CPU ops).

------------------------------------------------------------
Alternative (clearer) approaches:
1. Iterative bit-check (O(log n) time):
   - Examine bits from LSB to MSB, track previous bit and ensure current != previous.

2. String-based (convert to binary string):
   - Convert n to binary string and check `all(s[i] != s[i+1] for i in range(len(s)-1))`.
   - Simple but uses string allocation.

3. Bit-by-bit shifting (explicit):
   - Similar to iterative but using bit ops only (no string conversion).

------------------------------------------------------------
Complexity:
- Bit-trick: Time O(1) (bounded by word size), Space O(1)
- Iterative / string: Time O(log n) or O(bit-length), Space O(1) or O(log n) (string)

------------------------------------------------------------
Common pitfalls and gotchas:
- Operator precedence: write `(x & (x + 1)) == 0` — parentheses avoid confusion.
- Languages with signed shift behavior:
  - In Python, `>>` on non-negative ints is logical-like (fills with 0). For languages with arithmetic right shift on signed types (e.g., Java/C++ with signed ints), be careful with sign extension — use unsigned shifts or work with unsigned types.
- Make sure to handle `n` within 32/64-bit constraints in other languages (Python handles big ints).
- Don't rely on string conversion in a performance-critical inner loop — bit-trick is fastest and most elegant in interviews.

------------------------------------------------------------
Code (bit-trick + alternatives + tests)
"""
from typing import List


class Solution:
    # -------------------------
    # Optimal bit-trick solution
    # -------------------------
    def hasAlternatingBits(self, n: int) -> bool:
        # x becomes a sequence of 1s iff n had alternating bits
        x = n ^ (n >> 1)
        # check if x is of form 0b111...111  -> x & (x+1) == 0
        return (x & (x + 1)) == 0

    # -------------------------
    # Iterative (explicit) approach
    # -------------------------
    def hasAlternatingBits_iter(self, n: int) -> bool:
        prev = n & 1
        n >>= 1
        while n:
            cur = n & 1
            if cur == prev:
                return False
            prev = cur
            n >>= 1
        return True

    # -------------------------
    # String-based approach (easy to read)
    # -------------------------
    def hasAlternatingBits_str(self, n: int) -> bool:
        s = bin(n)[2:]
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return False
        return True


# -----------------------
# Quick tests / verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    tests = [
        (5, True),    # 101
        (7, False),   # 111
        (10, True),   # 1010
        (11, False),  # 1011
        (1, True),    # 1
        (2, True),    # 10
        (0b1010101, True),
        (0b100100, False),
    ]

    for n, expected in tests:
        out_trick = sol.hasAlternatingBits(n)
        out_iter = sol.hasAlternatingBits_iter(n)
        out_str = sol.hasAlternatingBits_str(n)
        ok = out_trick == expected and out_iter == expected and out_str == expected
        print(f"n={n} ({bin(n)}) -> trick:{out_trick}, iter:{out_iter}, str:{out_str} | expected:{expected} | {'OK' if ok else 'FAIL'}")
