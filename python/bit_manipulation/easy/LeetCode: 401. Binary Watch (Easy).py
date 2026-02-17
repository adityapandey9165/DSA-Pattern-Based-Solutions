"""
LeetCode: 401. Binary Watch (Easy)
Problem Link: https://leetcode.com/problems/binary-watch/
Author: Aditya Pandey
Date: 2026-02-17

Problem:
A binary watch has 4 LEDs for hours (0-11) and 6 LEDs for minutes (0-59).
Given an integer turnedOn representing the number of LEDs that are on,
return all possible times the watch could represent.

- Hour must not have a leading zero (e.g. "1:00" is valid, "01:00" not).
- Minutes must be two digits with leading zero if needed (e.g. "10:02").

Constraints:
0 <= turnedOn <= 10

------------------------------------------------------------
Pattern:
Enumeration + Bit Counting (popcount)

------------------------------------------------------------
How it works (intuition):
There are only 12 * 60 = 720 possible times. For each candidate time (h,m)
we can count the number of 1 bits in h and m (the number of LEDs lit).
If popcount(h) + popcount(m) == turnedOn, the time is valid.

In Python 3.8+, use `int.bit_count()` (fast builtin) to count 1 bits.
This is simple, very fast (constant work), easy to explain in interviews,
and robust.

------------------------------------------------------------
Alternative approaches:
1. Precompute lists of hours/minutes keyed by popcount
   - Slightly cleaner: compute all hours grouped by bit_count(h), minutes grouped by bit_count(m)
   - Then combine hours with minutes where counts sum to turnedOn.
   - Same asymptotic cost, can be marginally faster when reusing for multiple queries.

2. Generate combinations of LED indices (choose k LEDs out of 10)
   - More "combinatorial"; useful to demonstrate combinatorics but unnecessary here.
   - Requires validating resulting hour/minute values.

3. String-based: convert to binary and count '1' characters.
   - Works but `bit_count()` is clearer and faster.

------------------------------------------------------------
Complexity:
- Time: O(12 * 60) = O(1) (constant) — in practice ~720 popcounts.
- Space: O(result size) for storing answers.

------------------------------------------------------------
Common pitfalls:
- Wrong minute formatting — minutes must be `"{m:02d}"`.
- Forgetting hours cannot have leading zeros.
- Using string operations (less direct), or heavy combinatoric generation (unnecessary).
- For languages without `bit_count`, use builtin popcount or implement fast bit counting.

------------------------------------------------------------
Code (clean, idiomatic)
"""
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Early exit: turnedOn cannot exceed total LEDs (10)
        if turnedOn < 0 or turnedOn > 10:
            return []

        res: List[str] = []
        # iterate all possible times
        for h in range(12):       # hours 0..11
            for m in range(60):   # minutes 0..59
                # python 3.8+: use bit_count(); fallback to bin(x).count('1') if unavailable
                bits = h.bit_count() + m.bit_count()
                if bits == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    cases = [
        (1, ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]),
        (0, ["0:00"]),
        (9, []),
    ]

    for turnedOn, expected_hint in cases:
        out = sol.readBinaryWatch(turnedOn)
        print(f"turnedOn={turnedOn} -> {len(out)} results")
       
