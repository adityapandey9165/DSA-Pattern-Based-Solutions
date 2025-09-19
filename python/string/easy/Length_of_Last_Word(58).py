"""
LeetCode: 58. Length of Last Word (Easy)
Problem link: https://leetcode.com/problems/length-of-last-word/
Author: Aditya Pandey
Date: 2025-09-18

Problem:
Given a string s consisting of words and spaces, return the length of the last word
in the string. A word is a maximal substring consisting of non-space characters only.

Pattern: String processing — trim trailing spaces, then find last word

Approach (two common ways):
1) Without rstrip() approach (slice + split):
   - Trim trailing spaces by scanning from the end to find the last non-space index `l`.
   - Take s[:l+1].split(' ')[-1] and return its length.
   - Works, but `split(' ')` can produce empty strings if there are multiple consecutive spaces.

2) Recommended / robust approach:
   - Use Python string helpers:
     - `s.rstrip()` removes trailing spaces.
     - `s.rstrip().split()[-1]` uses split() without an argument (splits on any whitespace and ignores consecutive spaces).
   - Or find the last space using `rfind` and compute length directly:
     - `s = s.rstrip(); return len(s) - s.rfind(' ') - 1`

Time Complexity: O(n) where n = len(s)  
Space Complexity: O(1) extra if using `rfind` method; O(k) for split-based method where k is size of last word or number of tokens.

Common Mistakes:
- Not trimming trailing spaces (e.g., "Hello World   ").
- Using `split(' ')` which can produce empty strings for multiple spaces — prefer `split()` or `rfind`.
- Off-by-one when computing indices.

"""

from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Robust implementation:
        1) Trim trailing spaces with rstrip()
        2) Use rfind to locate the last space. If none, whole string is the last word.
        This runs in O(n) time and O(1) extra space.
        """
        s = s.rstrip()
        if not s:
            return 0
        last_space = s.rfind(' ')
        return len(s) - last_space - 1


# -----------------------
# Alternative  Without rstrip(), kept here for reference:
# -----------------------
class SolutionOriginal:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Original approach: manual scan to remove trailing spaces, then split on ' '.
        Note: split(' ') can produce empty tokens for consecutive spaces.
        """
        l = len(s) - 1
        while l >= 0 and s[l] == ' ':
            l -= 1
        if l < 0:
            return 0
        arr = s[:l + 1].split(' ')[-1]
        return len(arr)


# -----------------------
# Quick tests for revision
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    sol_orig = SolutionOriginal()

    tests = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("", 0),
        ("    ", 0),
        ("single", 6),
        ("a ", 1),
        ("a b  ", 1),
    ]

    for s, expected in tests:
        out = sol.lengthOfLastWord(s)
        out_orig = sol_orig.lengthOfLastWord(s)
        print(f"'{s}' -> {out} (expected={expected})   original -> {out_orig}")
