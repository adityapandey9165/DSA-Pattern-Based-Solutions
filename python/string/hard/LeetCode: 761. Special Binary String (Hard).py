"""
LeetCode: 761. Special Binary String (Hard)
Problem Link: https://leetcode.com/problems/special-binary-string/
Author: Aditya Pandey
Date: 2026-02-20

Problem:
A binary string is "special" if:
- It starts with '1' and ends with '0'
- The number of '1's equals the number of '0's
- For every prefix, number of '1's >= number of '0's

Given a special binary string s, a swap operation on two contiguous non-empty
special substrings keeps the string special. Return the lexicographically largest
string possible after any number of such swaps.

Example:
Input: "11011000"
Output: "11100100"

------------------------------------------------------------
Pattern:
Divide & Conquer (recursive decomposition) + Greedy (sort parts decreasingly)

------------------------------------------------------------
How it works (intuition):
- Any special string can be decomposed into a concatenation of primitive
  special substrings (balanced blocks where the running count returns to zero).
- For each primitive block of the form "1 + inner + 0", we can recursively
  transform its inner substring to the lexicographically largest special string,
  then the block becomes "1 + transformed_inner + 0".
- Among sibling primitive blocks at the same level, we can reorder them in any
  order (swapping adjacent special substrings keeps the whole string special).
  To get the lexicographically largest overall string, sort these transformed
  blocks in **decreasing** lexicographic order and concatenate them.

This gives a clean recursive algorithm:
1. Scan the string and split it into primitive special substrings by tracking a counter:
   - +1 for '1', -1 for '0'; whenever count hits 0 we found a primitive block s[start:i+1].
2. For each block, remove the outer '1' and '0', recursively process the inner substring,
   then rewrap: "1 + inner_processed + 0".
3. Sort all processed blocks in reverse order and join them.

Proof sketch of correctness:
- Reordering primitive blocks is valid because swapping contiguous special blocks
  keeps the global special property. Sorting them in descending lexicographic order
  maximizes the final string greedily because the leftmost characters weigh more
  in lexicographic comparison.

------------------------------------------------------------
Time & Space Complexity:
- Let n = len(s).
- Each level of recursion processes characters once. At each level we sort the list
  of sibling blocks; in worst case there can be many small blocks and sorting cost
  accumulates. A common upper bound given typical analysis is **O(n log n)** time
  (sorting dominates) and **O(n)** space for recursion + temporary storage.
- More precisely, the algorithm visits each character O(1) times across the recursion,
  and sorts partitions — worst-case behavior is bounded by O(n log n).

------------------------------------------------------------
Common pitfalls:
- Forgetting to process inner substring (`s[start+1:i]`) recursively — must strip outer bits.
- Sorting parts in ascending order (use descending / reverse sort).
- Off-by-one when slicing substring indices.
- Not using stable concatenation — use list append and `"".join()` for efficiency.
- Mistaking "balanced" for "special" — special requires prefix condition (but primitive blocks ensure it).

------------------------------------------------------------
Implementation (recursive, clean)
"""
from typing import List


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """
        Recursive decomposition: split s into primitive special blocks,
        recursively transform each block's inner part, sort blocks descending, join.
        """
        count = 0
        start = 0
        parts: List[str] = []

        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1

            # When count becomes zero we found a primitive special substring s[start:i+1]
            if count == 0:
                # Process inner substring recursively, strip outer '1' and '0'
                inner = self.makeLargestSpecial(s[start + 1 : i])
                # Rewrap the processed inner
                parts.append('1' + inner + '0')
                start = i + 1

        # Sort parts in descending lexicographic order and concatenate
        parts.sort(reverse=True)
        return ''.join(parts)


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("11011000", "11100100"),
        ("10", "10"),
        ("111000", "111000"),
        ("1101001100", None),  # example; expected computed by algorithm
    ]

    for s, expected in tests:
        out = sol.makeLargestSpecial(s)
        print(f"input: {s} -> output: {out}" + (f" | expected: {expected}" if expected else ""))
