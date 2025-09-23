"""
LeetCode: 28. Find the Index of the First Occurrence in a String (Implement strStr)
Problem link: https://leetcode.com/problems/implement-strstr/
Author: Aditya Pandey
Date: 2025-09-23

Description:
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
If needle is an empty string, return 0.

This file contains two solutions:
1) Sliding-window comparison (easy to explain, straightforward).
2) KMP (Knuth–Morris–Pratt) algorithm — O(H + N) worst-case, good interview follow-up.

When to use which:
- Use the sliding-window if interviewer allows a simple solution and you discuss worst-case complexity.
- Use (or mention) KMP if asked to improve worst-case time complexity or interviewer hints at repeated patterns.
"""

from typing import List


# -----------------------
# 1) Simple sliding-window solution (easy to explain)
# -----------------------
class SolutionSimple:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Slide a window of size len(needle) across haystack and compare substrings.
        Time: O((H - N + 1) * N) worst-case -> O(H * N) (bad for pathological cases like 'aaaa...a')
        Space: O(1)
        """
        if needle == "":
            return 0

        H, N = len(haystack), len(needle)
        if N > H:
            return -1

        # slide window [i : i+N)
        for i in range(H - N + 1):
            if haystack[i:i + N] == needle:
                return i
        return -1


# -----------------------
# 2) KMP (Knuth–Morris–Pratt) — linear-time worst-case
# -----------------------
class SolutionKMP:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Build lps (longest proper prefix which is also suffix) for needle.
        Then scan haystack once using lps to skip comparisons.
        Time: O(H + N), Space: O(N) for lps.
        """
        if needle == "":
            return 0

        H, N = len(haystack), len(needle)
        if N > H:
            return -1

        # Build lps array for needle
        lps = [0] * N
        length = 0  # length of the previous longest prefix suffix
        i = 1
        while i < N:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]  # fallback
                else:
                    lps[i] = 0
                    i += 1

        # KMP search
        i = j = 0  # i -> haystack index, j -> needle index
        while i < H:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == N:
                    return i - j  # match found
            else:
                if j != 0:
                    j = lps[j - 1]  # fallback in pattern
                else:
                    i += 1
        return -1


# -----------------------
# Quick tests (local verification)
# -----------------------
if __name__ == "__main__":
    tests = [
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "", 0),
        ("a", "a", 0),
        ("mississippi", "issip", 4),
        ("abababab", "abab", 0),
        ("abc", "abcd", -1),
        ("aaaab", "aab", 2),
    ]

    simple = SolutionSimple()
    kmp = SolutionKMP()

    for hay, ned, expected in tests:
        out_simple = simple.strStr(hay, ned)
        out_kmp = kmp.strStr(hay, ned)
        print(f"hay='{hay}', needle='{ned}' -> simple={out_simple}, kmp={out_kmp} (expected={expected})")
        assert out_simple == expected, f"Simple failed for {hay!r}, {ned!r}"
        assert out_kmp == expected, f"KMP failed for {hay!r}, {ned!r}"

    print("All tests passed.")
