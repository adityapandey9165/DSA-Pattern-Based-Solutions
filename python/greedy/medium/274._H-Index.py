"""
LeetCode: 274. H-Index (Medium)
Problem link: https://leetcode.com/problems/h-index/
Author: Aditya Pandey
Date: 2025-09-06

Problem:
Given an array of integers `citations` where citations[i] is the number of citations
a researcher received for their i-th paper, compute the researcher's h-index.
The h-index is the maximum value h such that the researcher has at least h papers
with at least h citations each.

Pattern: Sorting + Greedy / Prefix-check
- Sort citations in descending order and scan to find the largest position i
  such that citations[i] >= i+1 (1-based count). That i+1 is the h-index.

Approach (Sort & Scan):
1. Sort `citations` in **descending** order.
2. Iterate the sorted list with index `i` (0-based). For each position:
   - If `citations[i] >= i+1`, then there are at least (i+1) papers with >= (i+1) citations.
   - Keep increasing the candidate h-index while the condition holds.
3. When the condition breaks, return the current best `h`.

Why it works (intuition / short proof):
- After sorting descending, `citations[0]` is the largest citation count, `citations[1]` the second largest, etc.
- If at position `i` we have `citations[i] >= i+1`, it means there are (i+1) papers (indices 0..i) each with at least (i+1) citations. So h >= i+1 is feasible.
- The first time `citations[i] < i+1` occurs, we cannot have h = i+1 because there aren't (i+1) papers with >= (i+1) citations. Since we scanned from largest to smallest, the last valid `i+1` we recorded is the maximum possible h.

Alternative (linear) approach:
- Bucket counting (size n+1) to compute counts of citation frequencies capped at n, then accumulate from high to low to find h in O(n) time and O(n) space.

Time Complexity: O(n log n) due to sorting (O(n) for scan)
Space Complexity: O(1) extra (sorting may take O(n) depending on language / implementation)  
Alternative (bucket) approach: Time O(n), Space O(n)

Common Mistakes:
- Sorting ascending and applying wrong index condition (must be descending and compare to i+1).
- Off-by-one errors (mixing 0-based index with 1-based h count).
- Forgetting to cap very large citation counts for the bucket method (they can be treated as n).
- Returning immediately on first match without scanning (you must find the maximum i satisfying the condition).

Example Walkthrough:
citations = [3, 0, 6, 1, 5]
1. Sort desc -> [6, 5, 3, 1, 0]
2. i=0: 6 >= 1 -> h = 1
   i=1: 5 >= 2 -> h = 2
   i=2: 3 >= 3 -> h = 3
   i=3: 1 < 4  -> stop, final h = 3

Result: 3

"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Sort descending and find largest i with citations[i] >= i+1.
        """
        citations.sort(reverse=True)
        res = 0
        for i, val in enumerate(citations):
            if val >= i + 1:
                res = i + 1
            else:
                break
        return res


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3, 0, 6, 1, 5], 3),
        ([1, 3, 1], 1),
        ([100], 1),
        ([0,0,0], 0),
        ([4,4,4,4], 4),
    ]

    for arr, expected in tests:
        out = sol.hIndex(arr.copy())
        print(f"citations={arr} -> h-index={out} (expected={expected})")
