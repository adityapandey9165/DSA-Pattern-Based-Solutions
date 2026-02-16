"""
LeetCode: 190. Reverse Bits (Easy)
Problem Link: https://leetcode.com/problems/reverse-bits/
Author: Aditya Pandey
Date: 2026-02-16

------------------------------------------------------------
Problem:
Reverse the bits of a given 32-bit unsigned integer.

Example:
Input:  n = 00000010100101000001111010011100
Output: 00111001011110000010100101000000

Return the reversed 32-bit integer.

------------------------------------------------------------
Pattern:
Bit Manipulation / Bit Reversal
(Shift + Mask technique)

------------------------------------------------------------
Core Idea:

We process bits one by one:

1. Extract the least significant bit (LSB) using:
       n & 1

2. Shift result left to make space:
       res << 1

3. Append extracted bit using OR:
       res = (res << 1) | (n & 1)

4. Shift n right to process next bit:
       n >>= 1

Repeat 32 times (since input is 32-bit).

------------------------------------------------------------
How It Works Visually (Example 8-bit for simplicity):

n = 00001101

Step-by-step:
Take LSB → append to result → shift n
After 8 steps:
Result = 10110000

So bits are reversed.

------------------------------------------------------------
Why 32 iterations?
Because problem guarantees a 32-bit integer.
Even if leading bits are 0, they must be reversed too.

------------------------------------------------------------
Time Complexity:
O(1) → exactly 32 iterations

Space Complexity:
O(1)

------------------------------------------------------------
Common Mistakes:
- Forgetting to run loop exactly 32 times
- Not handling unsigned behavior (important in C++/Java)
- Forgetting to mask to 32 bits when needed
- Using string conversion in interviews (less optimal)

------------------------------------------------------------
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        # Ensure 32-bit behavior (important in some languages)
        n &= 0xFFFFFFFF

        res = 0

        for _ in range(32):
            # Shift result left to make space
            res = (res << 1) | (n & 1)

            # Shift n right to process next bit
            n >>= 1

        return res & 0xFFFFFFFF


# ------------------------------------------------------------
# Alternative Solutions (For Learning)
# ------------------------------------------------------------

def reverseBits_string(n: int) -> int:
    """
    Convert to 32-bit binary string,
    reverse it, then convert back to int.
    """
    b = f"{n:032b}"
    return int(b[::-1], 2)


def reverseBits_mask_swap(n: int) -> int:
    """
    Faster mask-based bit swapping approach.
    Useful when many calls are required.
    """
    n &= 0xFFFFFFFF
    n = ((n >> 1) & 0x55555555) | ((n & 0x55555555) << 1)
    n = ((n >> 2) & 0x33333333) | ((n & 0x33333333) << 2)
    n = ((n >> 4) & 0x0f0f0f0f) | ((n & 0x0f0f0f0f) << 4)
    n = ((n >> 8) & 0x00ff00ff) | ((n & 0x00ff00ff) << 8)
    n = ((n >> 16) & 0x0000ffff) | ((n & 0x0000ffff) << 16)
    return n & 0xFFFFFFFF


# ------------------------------------------------------------
# Quick Local Testing
# ------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    test = 0b00000010100101000001111010011100
    print("Original:", format(test, "032b"))
    reversed_val = sol.reverseBits(test)
    print("Reversed:", format(reversed_val, "032b"))

