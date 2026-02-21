"""
LeetCode: 762. Prime Number of Set Bits in Binary Representation (Easy)
Problem Link: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
Author: Aditya Pandey
Date: 2026-02-21

Problem:
Given two integers left and right (inclusive), count how many numbers in the range
[left, right] have a prime number of set bits (1s) in their binary representation.

Example:
Input: left = 6, right = 10
Binary:
6 -> 110 (two 1s)   -> 2 is prime -> count
7 -> 111 (three 1s) -> 3 is prime -> count
8 -> 1000 (one 1)   -> 1 not prime
9 -> 1001 (two 1s)  -> 2 is prime -> count
10 ->1010 (two 1s)  -> 2 is prime -> count
Output: 4

------------------------------------------------------------
Pattern:
Bit manipulation + Precomputation (popcount + primality set)

------------------------------------------------------------
How this solution works:
1. For each integer n in [left, right], compute the number of set bits (popcount).
   - In Python 3.8+, use `n.bit_count()` which is fast and implemented in C.
   - Alternatively use `bin(n).count("1")` (slower due to string allocation).
2. Check whether the popcount is prime. Since numbers in constraints have value up to 10^6
   (or 2^20-ish), the maximum number of set bits for a 32-bit integer is 32.
   So precompute all primes up to 32 and store them in a set for O(1) lookups.
3. Count how many n have popcount ∈ prime_set.

This is O((right-left+1) * popcount_cost) which is effectively O(N) with a small constant.

------------------------------------------------------------
Optimizations & Variants:
- Use `n.bit_count()` instead of `bin(n).count("1")` for speed.
- Precompute prime set once (primes up to 32).
- If you need extreme speed for huge ranges, consider bit-DP / convolution tricks, but
  for typical constraints this simple method is optimal and clear.

------------------------------------------------------------
Time Complexity:
- O(R-L+1) iterations; each iteration does O(1) work (bit_count & set lookup).
- Overall: O(N) where N = right - left + 1

Space Complexity:
- O(1) extra space (prime set is constant size)

------------------------------------------------------------
Common pitfalls:
- Checking primality per number without bounding the popcount (unnecessary work).
- Using string operations for popcount in tight loops (slower).
- Forgetting that 1 is not a prime.
- Not handling small ranges or left > right edge cases (rare).

------------------------------------------------------------
Implementation (clean, using bit_count and precomputed primes)
"""
from typing import Set


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Precomputed primes up to 32 (inclusive). 32 is upper bound for 32-bit integers.
        prime_set: Set[int] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

        count = 0
        for n in range(left, right + 1):
            # Use Python's fast popcount
            ones = n.bit_count()
            if ones in prime_set:
                count += 1
        return count


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ((6, 10), 4),
        ((10, 15), 5),
        ((1, 1), 0),    # 1 -> one 1 -> 1 is not prime
        ((2, 2), 1),    # 2 -> 10 -> 1 bit -> not prime -> result 0 (but 2 itself not counted)
        ((4, 4), 0),    # 4 -> 100 -> 1 bit -> not prime
        ((0, 0), 0),    # 0 -> 0 bits -> not prime
    ]

    for (L, R), expected in tests:
        out = sol.countPrimeSetBits(L, R)
        print(f"range=({L},{R}) -> {out} (expected {expected})")
