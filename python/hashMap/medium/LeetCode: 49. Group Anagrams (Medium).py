"""
LeetCode: 49. Group Anagrams (Medium)
Problem Link: https://leetcode.com/problems/group-anagrams/
Author: Aditya Pandey
Date: 2026-03-27

------------------------------------------------------------
Problem:
Given an array of strings strs, group the anagrams together.

An anagram is formed by rearranging the letters of another word.
Words that are anagrams should be placed in the same group.

------------------------------------------------------------
Pattern:
HashMap + Frequency Key

------------------------------------------------------------
Approach:
For each word:
1. Count frequency of each letter from 'a' to 'z'
2. Convert the frequency array into a tuple
3. Use that tuple as the key in a dictionary
4. Append the word to the group for that key

All anagrams have the same character frequency,
so they produce the same key.

------------------------------------------------------------
Why this works:
Example:
"eat" -> [1,0,0,0,1,0,...,1,...]
"tea" -> same frequency array
"ate" -> same frequency array

So they all map to the same dictionary key.

------------------------------------------------------------
Trade-offs / Other Approaches:

1. Sorting key
   key = "".join(sorted(word))

   Time: O(n * k log k)
   Space: O(n * k)

   Easy to understand, but slower because of sorting.

2. Frequency key (this solution)
   Time: O(n * k)
   Space: O(n * k)

   Faster than sorting and very interview-friendly.

------------------------------------------------------------
Things to Remember:
- Dictionary keys must be immutable, so use tuple(count)
- Do not use a list as a dict key
- Sorting is simpler, but frequency counting is more optimal
- This solution assumes lowercase English letters only

------------------------------------------------------------
Time Complexity:
O(n * k)

Space Complexity:
O(n * k)
"""


from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        base = ord("a")

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - base] += 1

            groups[tuple(count)].append(word)

        return list(groups.values())


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Expected: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

    print(sol.groupAnagrams([""]))
    # Expected: [[""]]

    print(sol.groupAnagrams(["a"]))
    # Expected: [["a"]]
