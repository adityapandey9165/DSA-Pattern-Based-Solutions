"""
LeetCode 1009 — Complement of Base 10 Integer
Difficulty: Easy
Topic: Bit Manipulation

Problem
-------
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

Approach
--------
1. Create a mask with all bits = 1 having same length as n.
2. XOR the mask with n to flip the bits.

Example:
n = 5 -> 101
mask = 111

101
^111
----
010 -> 2

Edge Case
---------
n = 0 → return 1

Time Complexity
---------------
O(log n)

Space Complexity
----------------
O(1)
"""


class Solution:
    def bitwiseComplement(self, n: int) -> int:

        # edge case
        if n == 0:
            return 1

        mask = 1

        # create mask of 111..111
        while mask <= n:
            mask <<= 1

        mask -= 1

        return n ^ mask


# Example usage (for local testing)
if __name__ == "__main__":

    sol = Solution()

    test_cases = [5, 7, 10, 0]

    for n in test_cases:
        print(f"n = {n}, complement = {sol.bitwiseComplement(n)}")
