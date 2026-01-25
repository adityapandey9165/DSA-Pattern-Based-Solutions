"""
LeetCode: 1984. Minimum Difference Between Highest and Lowest of K Scores (Easy)
Problem Link: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
Author: Aditya Pandey
Date: 2026-01-19

--------------------------------------------------
Problem:
Given an integer array `nums` and an integer `k`,
pick `k` elements such that the difference between
the maximum and minimum of these elements is minimized.

Return that minimum difference.

--------------------------------------------------
Pattern:
1. Sorting + Sliding Window
2. Frequency Array + Sliding Window (Counting Sort Idea)

--------------------------------------------------
Approach 1: Sorting + Sliding Window (Recommended)

Idea:
- Sort the array
- Any valid group of k elements must be contiguous after sorting
- Slide a window of size k and compute:
      nums[i + k - 1] - nums[i]

Steps:
1. If k == 1 → answer is 0
2. Sort nums
3. Iterate over all windows of size k
4. Track minimum difference

Time Complexity:
O(n log n)

Space Complexity:
O(1) extra (ignoring sort space)

--------------------------------------------------
Approach 2: Frequency Array + Sliding Window

Idea:
- Instead of sorting, count frequencies (values up to 10^5)
- Slide a window over the value range
- Maintain count of elements in the window
- When count ≥ k, update answer

This is useful when:
- Value range is limited
- n is very large
- Sorting cost needs to be avoided

Time Complexity:
O(n + K), where K = max(nums) ≤ 10^5

Space Complexity:
O(K)

--------------------------------------------------
Pros / Cons / Trade-offs:

Sorting Approach:
✔ Simple and clean
✔ Easy to explain in interviews
✔ Preferred unless constraints are huge
✘ O(n log n)

Frequency Approach:
✔ Linear time
✔ Avoids sorting
✔ Good for bounded values
✘ Extra memory
✘ More complex logic

--------------------------------------------------
Interview Tip:
Start with sorting approach.
Mention frequency optimization only if interviewer asks.

--------------------------------------------------
"""

from typing import List


class Solution:
    # -------- Approach 1: Sorting --------
    def minimumDifference_sort(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        nums.sort()
        res = float('inf')

        for i in range(len(nums) - k + 1):
            res = min(res, nums[i + k - 1] - nums[i])

        return res

    # -------- Approach 2: Frequency + Sliding Window --------
    def minimumDifference_freq(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        MAX_VAL = 10**5
        freq = [0] * (MAX_VAL + 1)

        for num in nums:
            freq[num] += 1

        left = 0
        count = 0
        res = float('inf')

        for right in range(MAX_VAL + 1):
            count += freq[right]
            while count >= k:
                res = min(res, right - left)
                count -= freq[left]
                left += 1

        return res


# -----------------------
# Local Testing
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [9, 4, 1, 7]
    k = 2

    print(sol.minimumDifference_sort(nums, k))  # Expected: 2
    print(sol.minimumDifference_freq(nums, k))  # Expected: 2
