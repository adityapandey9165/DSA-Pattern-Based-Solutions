"""
LeetCode: 14. Longest Common Prefix (Easy)
Problem link: https://leetcode.com/problems/longest-common-prefix/
Author: Aditya Pandey
Date: 2025-09-20

Problem:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Pattern:
- String processing
- Shrinking prefix until it matches all strings

Approach:
1. Take the first string `s` as the initial candidate prefix.
2. For each word in the list:
   - While the current prefix `s` does not match the start of that word, keep shrinking `s` from the end.
   - If `s` becomes empty at any point, return "" (no common prefix).
3. Return the final `s`.

Time Complexity: O(n * m)  
- n = number of strings  
- m = length of the shortest string  
In the worst case, we compare characters until the prefix shrinks.  

Space Complexity: O(1) (in-place shrinking of prefix).  

Common Interview Variants:
- Using vertical scanning (character by character across all strings).  
- Using divide & conquer approach (merge prefixes pairwise).  
- Binary search on prefix length.  
- Trick question: handling edge cases like empty list, or strings of very different lengths.  

"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            # shrink prefix until it matches start of word
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


# -----------------------
# Quick tests
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], ""),
        (["interspecies","interstellar","interstate"], "inters"),
        (["a"], "a"),
        (["ab","a"], "a"),
        ([""], ""),
    ]
    for strs, expected in tests:
        print(f"{strs} -> {sol.longestCommonPrefix(strs)} (expected={expected})")
