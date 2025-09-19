"""
LeetCode: 13. Roman to Integer (Easy)
Problem link: https://leetcode.com/problems/roman-to-integer/
Author: Aditya Pandey
Date: 2025-09-18

Problem:
Convert a Roman numeral string to an integer. Roman numerals are represented by:
I (1), V (5), X (10), L (50), C (100), D (500), M (1000).
Some numerals use subtraction, e.g., IV = 4, IX = 9, XL = 40, etc.

Pattern: Left-to-right scan with subtraction trick
- Add the value of each symbol.
- If a symbol has greater value than the previous symbol, subtract twice the previous
  (because we already added it once before, so subtracting twice effectively turns
  "+prev + curr" into "curr - prev").

Example:
s = "MCMXCIV"
Scan:
M (1000) -> res = 1000
C (100)  -> res = 1100
M (1000) -> curr > prev (1000>100) => res += 1000 - 2*100 = 1800
X (10)   -> res += 10 = 1810
C (100)  -> curr > prev -> res += 100 - 2*10 = 1890
I (1)    -> res += 1 = 1891
V (5)    -> curr > prev -> res += 5 - 2*1 = 1894

Time Complexity: O(n) — single pass over the input string
Space Complexity: O(1) — constant extra space

Common Mistakes:
- Not handling subtraction cases (e.g., treating "IV" as 1+5 instead of 4).
- Accessing previous character incorrectly (off-by-one indices).
- Using multiple if-else chains instead of a map (messy and error-prone).

"""

from typing import Dict


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert Roman numeral `s` to integer.
        Uses a left-to-right scan with a mapping and subtraction when current > previous.
        """
        # mapping Roman numerals to integers
        value: Dict[str, int] = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        prev_val = 0  # numeric value of previous character (0 for none)

        for ch in s:
            curr = value.get(ch, 0)
            res += curr
            # if current is greater than previous, we have seen a subtraction case
            if curr > prev_val:
                # we already added prev_val once, so subtract it twice to convert +prev +curr -> curr - prev
                res -= 2 * prev_val
            prev_val = curr

        return res


if __name__ == "__main__":
    # quick tests for revision
    sol = Solution()
    tests = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),       # L=50, V=5, III=3
        ("MCMXCIV", 1994),   # M=1000, CM=900, XC=90, IV=4
        ("XL", 40),
        ("CD", 400),
    ]

    for s, expected in tests:
        out = sol.romanToInt(s)
        print(f"{s} -> {out} (expected: {expected})")
