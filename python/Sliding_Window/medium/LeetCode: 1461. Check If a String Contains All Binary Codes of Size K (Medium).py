"""
LeetCode: 1461. Check If a String Contains All Binary Codes of Size K (Medium)
Problem Link: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
Author: Aditya Pandey
Date: 2026-02-23

Problem:
Given a binary string s and an integer k, return true if every binary code
(of length k) is a substring of s. Otherwise return false.

Example:
s = "00110110", k = 2 -> True (00,01,10,11 all appear)

Constraints:
- 1 <= k <= 20 (typical)
- If k > len(s) answer is always False

------------------------------------------------------------
Pattern:
Sliding Window + Hash Set
Optimization: Rolling bitmask (constant-time update per char)

------------------------------------------------------------
Idea / Intuition:
There are 2^k possible binary strings of length k. We must check whether
all of them appear as contiguous substrings in s. Two practical ways:

1) Simple substring set:
   - Enumerate every substring s[i:i+k] and add to a set.
   - At the end check if set size == 2^k.

   Pros: Very simple and readable.
   Cons: Substring slicing costs O(k) per substring → O(n*k) time.

2) Rolling bitmask (optimal):
   - Treat each k-length window as an integer (bitmask).
   - Update window in O(1) when sliding: shift left, add new bit, mask low k bits.
   - Store integer masks in a set. Check count == 2^k.

   Pros: O(n) time, lower constant factors, avoids substring allocation.
   Cons: Slightly more bit-trick code to explain.

------------------------------------------------------------
Edge Cases:
- If k > len(s) → return False immediately.
- If k is large (e.g., >20), 2^k becomes large — but constraints usually keep k small.
- Duplicate substrings should only be counted once (use set).

------------------------------------------------------------
Complexity:
- Naive substring-set: Time O(n * k), Space O(min(2^k, n))
- Rolling bitmask: Time O(n), Space O(min(2^k, n))

------------------------------------------------------------
Implementation (both versions)
"""
from typing import Set


class Solution:
    # -------------------------
    # Simple substring set (easy to explain)
    # -------------------------
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        seen: Set[str] = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i + k])
            # early break if we've seen all combos
            if len(seen) == (1 << k):
                return True
        return len(seen) == (1 << k)

    # -------------------------
    # Optimized: rolling bitmask (recommended)
    # -------------------------
    def hasAllCodes_optimized(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        needed = 1 << k
        seen: Set[int] = set()
        mask = needed - 1  # keep only k bits
        window = 0

        for i, ch in enumerate(s):
            # add bit to window
            window = ((window << 1) & mask) | (1 if ch == '1' else 0)
            # once we've filled first k bits, start recording
            if i >= k - 1:
                seen.add(window)
                if len(seen) == needed:
                    return True  # early exit when all found

        return len(seen) == needed


# -----------------------
# Quick tests / verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("00110110", 2, True),
        ("0110", 1, True),
        ("0110", 2, False),
        ("0000000000", 3, False),
        ("01", 2, False),
    ]

    for s, k, expected in tests:
        out1 = sol.hasAllCodes(s, k)
        out2 = sol.hasAllCodes_optimized(s, k)
        ok = (out1 == expected) and (out2 == expected)
        print(f"s={s!r}, k={k} -> set:{out1}, opt:{out2}, expected:{expected} | {'OK' if ok else 'FAIL'}")
