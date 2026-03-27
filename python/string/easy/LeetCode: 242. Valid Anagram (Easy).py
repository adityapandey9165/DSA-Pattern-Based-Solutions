"""
LeetCode: 242. Valid Anagram (Easy)
Problem Link: https://leetcode.com/problems/valid-anagram/
Author: Aditya Pandey
Date: 2026-03-26

------------------------------------------------------------
Problem:
Given two strings s and t, return True if t is an anagram of s,
otherwise return False.

An anagram means both strings contain the same characters
with the same frequency.

------------------------------------------------------------
Pattern:
Frequency Counting / Hashing

------------------------------------------------------------
Approach (Optimal - Array Count):
Since input contains only lowercase letters (a–z),
we use a fixed size array of 26.

Steps:
1. If lengths differ → return False
2. Count characters:
   - increment for s
   - decrement for t
3. If all values are zero → anagram

------------------------------------------------------------
Why this works:
- Each character cancels itself out
- If both strings have same frequency → final array is all zeros

------------------------------------------------------------
Time Complexity:
O(n)

Space Complexity:
O(1)  (since 26 fixed size)

------------------------------------------------------------
Trade-offs / Other Approaches:

1. Sorting
   sorted(s) == sorted(t)

   Time: O(n log n)
   Space: O(n)
   ✔ Simple to write
   ❌ Slower

------------------------------------------------------------

2. HashMap (Counter)

   from collections import Counter
   Counter(s) == Counter(t)

   Time: O(n)
   Space: O(n)

   ✔ Works for any charset (Unicode)
   ❌ Extra space

------------------------------------------------------------

3. This Approach (Best for interviews)
   ✔ O(n) time
   ✔ O(1) space
   ✔ Very fast

------------------------------------------------------------
Things to Remember:
- Always check length first (quick fail)
- This works only for fixed charset (a-z)
- Use ord() carefully:
      index = ord(char) - ord('a')
- For Unicode → use Counter instead

------------------------------------------------------------
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = [0] * 26
        base = ord('a')

        for i in range(len(s)):
            count[ord(s[i]) - base] += 1
            count[ord(t[i]) - base] -= 1

        return all(v == 0 for v in count)


# -----------------------
# Quick tests
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
    print(sol.isAnagram("aacc", "ccac"))        # False
