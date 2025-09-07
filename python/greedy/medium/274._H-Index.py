"""
LeetCode: 274. H-Index (Medium)
Problem link: https://leetcode.com/problems/h-index/
Author: Aditya Pandey
Date: 2025-09-07

This file contains two solutions for the H-Index problem:

1) Sort & Scan (O(n log n))
   - Simple and intuitive: sort citations in descending order and find the largest
     i such that citations[i] >= i + 1.

2) Bucket / Counting (O(n))
   - Linear-time method using bucketing (cap counts > n into bucket n) and then
     scanning from high to low to find the h-index.

Keep both for revision:
- Use the sort version when you want a quick and easy implementation.
- Use the bucket version when you care about linear-time performance.
"""

from typing import List
from collections import defaultdict


class Solution:
    # -----------------------
    # Approach 1: Sort & Scan
    # Time: O(n log n), Space: O(1) extra (sorting cost depends on language)
    # -----------------------
    def hIndex_sort(self, citations: List[int]) -> int:
        """
        Sort citations in descending order and find the largest index i where
        citations[i] >= i + 1. Return i + 1 as the h-index.
        """
        # Defensive: empty input
        if not citations:
            return 0

        citations_sorted = sorted(citations, reverse=True)
        res = 0
        for i, val in enumerate(citations_sorted):
            if val >= i + 1:
                res = i + 1
            else:
                break
        return res

    # -----------------------
    # Approach 2: Bucket / Counting (O(n))
    # Time: O(n), Space: O(n)
    # -----------------------
    def hIndex_bucket(self, citations: List[int]) -> int:
        """
        Bucket/counting approach:
        - Use buckets 0..n where bucket[n] counts citations >= n.
        - Accumulate counts from n down to 0; when accumulated >= i, return i.
        """
        n = len(citations)
        if n == 0:
            return 0

        # buckets: index x stores number of papers with exactly x citations (for x < n)
        # bucket n stores number of papers with >= n citations
        buckets = [0] * (n + 1)
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1

        papers = 0
        for i in range(n, -1, -1):
            papers += buckets[i]
            if papers >= i:
                return i
        return 0

    # -----------------------
    # Default API method: choose one to call (both are available for study)
    # Here we use the O(n) bucket method by default for efficiency.
    # -----------------------
    def hIndex(self, citations: List[int]) -> int:
        """
        Default method used by the repo / tests. Uses the O(n) bucket solution.
        """
        return self.hIndex_bucket(citations)


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3, 0, 6, 1, 5], 3),
        ([1, 3, 1], 1),
        ([100], 1),
        ([0, 0, 0], 0),
        ([4, 4, 4, 4], 4),
        ([0], 0),
        ([], 0),
        ([10, 8, 5, 4, 3], 4),
    ]

    print("Testing both implementations (sort & bucket):\n")
    for arr, expected in tests:
        out_sort = sol.hIndex_sort(arr.copy())
        out_bucket = sol.hIndex_bucket(arr.copy())
        out_default = sol.hIndex(arr.copy())
        print(f"citations={arr}")
        print(f"  expected = {expected}")
        print(f"  sort    -> {out_sort}")
        print(f"  bucket  -> {out_bucket}")
        print(f"  default -> {out_default}")
        print("-" * 50)
