"""
LeetCode: 1680. Concatenation of Consecutive Binary Numbers (Medium)
Problem Link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
Author: Aditya Pandey
Date: 2026-02-28

Problem:
Concatenate the binary representations of all integers from 1 to n in order,
and return the decimal value of the resulting binary string modulo 10^9 + 7.

For example, n = 3:
"1" + "10" + "11" -> "11011" (binary) -> 27 (decimal)

------------------------------------------------------------
Pattern:
Bit Manipulation / Modular arithmetic / Iterative simulation

------------------------------------------------------------
How this solution works (intuition):
- Let `res` hold the current concatenated value (as an integer).
- For each new integer `i` from 1..n:
  1. Find the number of bits `l` needed to represent `i` (that is, `i.bit_length()`).
  2. Shift `res` left by `l` bits to make room for `i`.
  3. Bitwise-OR `i` into the low bits: `res = (res << l) | i`.
  4. Reduce modulo `MOD` to avoid huge integers.
- Return `res % MOD`.

Key micro-optimization (used in first impl):
- Instead of calling `i.bit_length()` each iteration, increment `l` when `i` is a power of two:
  when `i & (i-1) == 0`, `i` increases its required bit-length by 1 (1,2,4,8,...).

------------------------------------------------------------
Why modulo at each step?
- The concatenated integer grows exponentially in bits; taking `% MOD` after every step
  keeps values small and prevents unnecessary big-int work while preserving the final result.

------------------------------------------------------------
Time Complexity:
- O(n) iterations. Each iteration does O(1) bit ops + modular arithmetic.
- Overall: O(n)

Space Complexity:
- O(1) extra space

------------------------------------------------------------
Common pitfalls:
- Forgetting to shift by the correct number of bits (`l`).
- Operator precedence: use parentheses `((res << l) | i) % MOD`.
- Not taking modulo each iteration may cause large intermediate integers (slow).
- Off-by-one when computing bit-length; prefer `i.bit_length()` or the power-of-two test.

------------------------------------------------------------
Implementations:
- Method 1: use incremental `l` and power-of-two test (few integer ops per loop).
- Method 2: use `i.bit_length()` directly (clear and concise).
"""

from typing import Optional


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        Implementation using incremental bit-length `l`:
        increase `l` by 1 when i is a power of two.
        """
        MOD = 10**9 + 7
        res = 0
        l = 0  # current bit length for i (will increase when i is power of two)

        for i in range(1, n + 1):
            # if i is power of two (1,2,4,8,...), then bit length increases by 1
            if (i & (i - 1)) == 0:
                l += 1
            # shift left by l bits and append i, then mod to keep numbers small
            res = ((res << l) | i) % MOD

        return res

    def concatenatedBinary_bitlength(self, n: int) -> int:
        """
        Alternative implementation using i.bit_length() each iteration.
        Slightly clearer; performance is similar for typical constraints.
        """
        MOD = 10**9 + 7
        res = 0
        for i in range(1, n + 1):
            l = i.bit_length()
            res = ((res << l) | i) % MOD
        return res


# -----------------------
# Quick tests / local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        (1, 1),     # "1" -> 1
        (2, 6),     # "110" -> 6
        (3, 27),    # "11011" -> 27
        (4, 220),   # "11011100" -> 220
        (6, 39675), # known sample
    ]

    for n, expected in tests:
        out = sol.concatenatedBinary(n)
        out2 = sol.concatenatedBinary_bitlength(n)
        ok = (out == expected) and (out2 == expected)
        print(f"n={n} -> res: {out}, alt: {out2}, expected: {expected} | {'OK' if ok else 'FAIL'}")
