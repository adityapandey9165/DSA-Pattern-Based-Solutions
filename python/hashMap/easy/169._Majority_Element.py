"""
LeetCode: 169. Majority Element (Easy)
Problem link: https://leetcode.com/problems/majority-element/
Author: Aditya Pandey
Date: 2025-09-04

Problem:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than floor(n / 2) times.
You may assume that the majority element always exists in the array.

Approaches:
1) Hash map / Frequency count (intuitive)
   - Count occurrences of each value; the one with count > n//2 is the majority.
   - Time: O(n), Space: O(n)

2) Boyer–Moore Voting Algorithm (optimal)
   - Maintain a candidate and a counter.
   - Increment counter when same as candidate, decrement otherwise.
   - When counter drops to 0, pick new candidate.
   - At the end the candidate is the majority (guaranteed to exist).
   - Time: O(n), Space: O(1)

Time Complexity: O(n)
Space Complexity: O(1) for Boyer-Moore, O(n) for hashmap approach.

Common Mistakes:
- Not handling negative numbers or zeros specially (not needed here).
- Using integer division incorrectly when checking n/2 (use n // 2).
- Assuming majority element exists in other variants (here it's guaranteed).
"""

from typing import List
from collections import defaultdict


class Solution:
    def majorityElement_hashmap(self, nums: List[int]) -> int:
        """
        Simple hashmap-count approach.
        Returns the majority element (count > n//2).
        """
        n = len(nums)
        freq = defaultdict(int)
        for x in nums:
            freq[x] += 1
            if freq[x] > n // 2:
                return x
        # Problem guarantees existence, but return something safe:
        return nums[0]

    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm (O(n) time, O(1) space).
        Returns the majority element.
        """
        # Phase 1: find a candidate
        candidate = None
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
                count = 1
            elif x == candidate:
                count += 1
            else:
                count -= 1

        # If majority is guaranteed to exist, candidate is the answer.
        # If not guaranteed, we would do a second pass to verify.
        return candidate


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([-1, -1, -1, 0, 0], -1),
    ]

    for arr, expected in tests:
        ans_hash = sol.majorityElement_hashmap(arr.copy())
        ans_bm = sol.majorityElement(arr.copy())
        print(f"arr={arr}  expected={expected}  hashmap={ans_hash}  boyer-moore={ans_bm}")
