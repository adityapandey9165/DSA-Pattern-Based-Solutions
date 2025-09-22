"""
LeetCode: 151. Reverse Words in a String (Medium)
Problem link: https://leetcode.com/problems/reverse-words-in-a-string/
Author: Aditya Pandey
Date: 2025-09-20

Contains:
- Solution.reverseWords (explicit, interview-friendly, no split())
- Solution.reverseWords_pythonic (idiomatic one-liner using split())

Both are O(n) time and O(n) space (output).
"""

from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Interview-friendly implementation without using split():
        - Scan from the end to extract words (skipping spaces).
        - Append words to list and join with single space.
        Time: O(n), Space: O(n)
        """
        n = len(s)
        i = n - 1
        words: List[str] = []

        while i >= 0:
            # skip trailing / intermediate spaces
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break
            # find the start of the word
            j = i
            while j >= 0 and s[j] != ' ':
                j -= 1
            # s[j+1 : i+1] is the word
            words.append(s[j + 1 : i + 1])
            # continue from j-1
            i = j - 1

        return " ".join(words)

    def reverseWords_pythonic(self, s: str) -> str:
        """
        Pythonic one-liner using split() which trims and collapses whitespace.
        Use this when language idioms are allowed/encouraged.
        """
        return " ".join(s.split()[::-1])


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("", ""),
        ("    ", ""),
        ("single", "single"),
        ("  multiple   spaces  around  ", "around spaces multiple"),
    ]

    for inp, expected in tests:
        out_default = sol.reverseWords(inp)
        out_py = sol.reverseWords_pythonic(inp)
        assert out_default == expected, f"default failed: {inp!r} -> {out_default!r} expected {expected!r}"
        assert out_py == expected, f"pyth failed:    {inp!r} -> {out_py!r}    expected {expected!r}"
    print("All tests passed for both implementations.")
