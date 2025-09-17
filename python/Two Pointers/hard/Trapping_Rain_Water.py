"""
LeetCode: 42. Trapping Rain Water (Hard)
Problem link: https://leetcode.com/problems/trapping-rain-water/
Author: Aditya Pandey
Date: 2025-09-17

This file contains two canonical approaches to compute trapped water:

1) Prefix/Right-max arrays (precompute left/right max) — O(n) time, O(n) space
2) Two-pointer (left/right scan with running max) — O(n) time, O(1) space

Both are useful to know in interviews: the first is straightforward to derive;
the second is the optimal, elegant pattern to memorize.
"""

from typing import List


# -------------------------
# Approach 1: Precompute right-max (and implicitly left-max while iterating)
# (Equivalent to computing left_max[] and right_max[] and summing min(left,right)-height)
# -------------------------
class SolutionPrefix:
    def trap(self, height: List[int]) -> int:
        """
        Precompute the maximum to the right of each index, then walk left-to-right,
        maintaining left max as `m`. For each index, water = max(0, min(left_max, right_max[i]) - height[i]).
        """
        if not height:
            return 0

        n = len(height)
        # right[i] = max height to the right of i (strictly to the right)
        right = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])

        res = 0
        left_max = 0  # maximum to the left of current index
        for i in range(n):
            # water at i is min(left_max, right[i]) - height[i]
            trapped = min(left_max, right[i]) - height[i]
            if trapped > 0:
                res += trapped
            # update left_max after computing trapped for this index
            if height[i] > left_max:
                left_max = height[i]

        return res


# -------------------------
# Approach 2: Two-pointer (optimal O(1) extra space)
# -------------------------
class SolutionTwoPointer:
    def trap(self, height: List[int]) -> int:
        """
        Two-pointer approach:
        - Maintain l and r pointers and the current left_max and right_max.
        - Move the pointer whose side has smaller max, because trapped water there
          is limited by that smaller max.
        - Accumulate right_max - height[r] or left_max - height[l] as appropriate.
        """
        if not height:
            return 0

        n = len(height)
        l, r = 0, n - 1
        left_max, right_max = height[l], height[r]
        res = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += max(0, left_max - height[l])
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += max(0, right_max - height[r])

        return res


# -------------------------
# Quick tests for revision
# -------------------------
if __name__ == "__main__":
    tests = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
        ([], 0),
        ([1,1,1,1], 0),
        ([5,4,1,2], 1),
    ]

    sol1 = SolutionPrefix()
    sol2 = SolutionTwoPointer()

    for arr, expected in tests:
        out1 = sol1.trap(arr.copy())
        out2 = sol2.trap(arr.copy())
        print(f"height={arr}")
        print(f"  prefix  -> {out1} (expected={expected})")
        print(f"  two-ptr -> {out2} (expected={expected})")
        print("-" * 50)


# -------------------------
# Interview notes: patterns & common questions
# -------------------------
#
# Pattern to remember:
# - This is a classic "water trapping" problem: at index i the trapped amount is
#       max(0, min(max_left[i], max_right[i]) - height[i])
#   The two core ways to implement this are:
#   1) Precompute max_left and max_right arrays (or compute one side on the fly and the other in an array).
#   2) Two-pointer scan keeping left_max and right_max — uses O(1) extra space.
#
# Why two-pointer works (intuition):
# - If left_max < right_max, then water trapped at left is bounded by left_max (not by right_max),
#   so we can safely process and move left pointer. Symmetrically for the right side.
#
# Common interview follow-ups / questions:
# - Explain the intuition for the two-pointer method and prove it doesn't miss cases.
# - How would you compute the total trapped water if the bars are given as floating heights?
# - What changes if diagonals or 2D terrain (matrix) are considered? (That becomes a different, harder problem—use priority queue / BFS from boundary.)
# - Can you produce the water-trapped per-index array (not just the sum)? (Yes—store min(left_max,right_max)-height[i].)
# - Memory vs time trade-offs: when to prefer O(n) extra arrays vs O(1) two-pointer?
# - How does this relate to the "largest rectangle in histogram" or "maximal rectangle" problems?
#
# Common mistakes:
# - Mixing up when to update left_max/right_max vs when to compute trapped water (order matters).
# - In two-pointer approach, moving the wrong pointer (must move the side with smaller max).
# - Forgetting to handle empty input or single-element arrays.
#
# Complexity:
# - Time: O(n)
# - Space:
#    - Prefix/Right-array: O(n) extra
#    - Two-pointer: O(1) extra
#-------------------------
