"""
LeetCode: 12. Integer to Roman (Medium)
Problem link: https://leetcode.com/problems/integer-to-roman/
Author: Aditya Pandey
Date: 2025-09-18

Problem:
Convert an integer to a Roman numeral. Roman numerals are built from these symbols:
I (1), V (5), X (10), L (50), C (100), D (500), M (1000) plus subtractive pairs like IV (4), IX (9), XL (40), XC (90), CD (400), CM (900).
Input constraints: 1 <= num <= 3999 (typical LeetCode bounds).

Pattern: Greedy with descending value list
- Pre-store all relevant numeral values including subtractive combinations.
- Greedily subtract the largest possible value from `num` and append its Roman symbol until `num` becomes 0.
- This is effectively converting `num` using base-like greedy decomposition with a custom value set.

Time Complexity: O(1) (bounded by the number of Roman symbols; in practice very small)  
Space Complexity: O(1) extra (output string excluded)

Common Mistakes:
- Failing to include subtractive cases (4, 9, 40, 90, 400, 900). Without them you'll produce invalid numerals.
- Using wrong ordering (must try the largest values first).
- Not handling bounds (LeetCode usually restricts to 1..3999).
"""

from typing import Dict, List


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert integer `num` to Roman numeral using greedy subtraction of values.
        """
        # Map of base and subtractive Roman values to symbols
        mapping: Dict[int, str] = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        # Create a descending sorted list of keys for greedy subtraction
        values: List[int] = sorted(mapping.keys(), reverse=True)

        res: List[str] = []
        for v in values:
            # While we can subtract v from num, append the corresponding symbol
            while num >= v:
                num -= v
                res.append(mapping[v])
            if num == 0:
                break

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()

    tests = [
        (3, "III"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),     # L=50, V=5, III=3
        (1994, "MCMXCIV"), # M=1000, CM=900, XC=90, IV=4
        (40, "XL"),
        (400, "CD"),
        (3999, "MMMCMXCIX"),
    ]

    for n, expected in tests:
        out = sol.intToRoman(n)
        print(f"{n} -> {out} (expected: {expected})")
