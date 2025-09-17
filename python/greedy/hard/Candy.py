"""
LeetCode: 135. Candy (Hard)
Problem link: https://leetcode.com/problems/candy/
Author: Aditya Pandey
Date: 2025-09-17

Problem:
There are n children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subject to the following requirements:
  1. Each child must have at least one candy.
  2. Children with a higher rating get more candies than their immediate neighbors.

Return the minimum number of candies you need to distribute.

Pattern: Two-pass Greedy (Left-to-right & Right-to-left)

Approach (Intuition + Algorithm):
- The constraints are local: each child's candy count depends on neighbors.
- A clean and optimal solution is a two-pass greedy:
  1. Initialize an array `candies = [1] * n` because every child must get at least one.
  2. Left-to-right pass: ensure the left neighbor constraint.
     - If ratings[i] > ratings[i-1], set candies[i] = candies[i-1] + 1.
  3. Right-to-left pass: ensure the right neighbor constraint while preserving left-side gains.
     - If ratings[i] > ratings[i+1], set candies[i] = max(candies[i], candies[i+1] + 1).
- The `max` in the second pass ensures both neighbor constraints are satisfied.
- Return sum(candies).

Why this problem is considered *hard* (what to remember):
- Local constraints on both sides make a single greedy direction insufficient. A naive single-pass greedy can break the other neighbor condition.
- The correct insight is to combine two directional passes and use `max` in the second pass to preserve previous work — that insight is non-obvious unless you’ve seen pattern before.
- Proving correctness needs the observation that the left-to-right pass computes minimal candies satisfying left-neighbor constraints, and the right-to-left pass fixes any violations relative to the right neighbor without breaking the left guarantees.
- There are other (more complex) solutions (sorting by rating with union/segments, slope-based single-pass), but they are more error-prone — the two-pass method is simple, optimal, and interview-friendly once explained.

Time Complexity: O(n) — two linear passes  
Space Complexity: O(n) — extra array for candies (output not counted if you overwrite input; otherwise O(1) is not straightforward)

Common Mistakes / Interview traps:
- Trying to do it with a single directional greedy without proof — leads to wrong answers on patterns like peaks/valleys.
- Forgetting to use `max` in the second pass — you may overwrite a correct left-to-right assignment.
- Mis-handling equal ratings — equal ratings must not force extra candies.
- Thinking sorting ratings then assigning candies works straightforwardly (it can, but requires careful grouping and is more complex).

Example Walkthrough:
ratings = [1, 0, 2]
n = 3
candies = [1,1,1]

Left-to-right:
i=1: ratings[1]=0 <= ratings[0]=1 -> candies[1]=1
i=2: ratings[2]=2 > ratings[1]=0 -> candies[2]=candies[1]+1=2
candies after L->R = [1,1,2]

Right-to-left:
i=1: ratings[1]=0 not > ratings[2]=2 -> no change
i=0: ratings[0]=1 > ratings[1]=0 -> candies[0]=max(1, candies[1]+1=2)=2
Final candies = [2,1,2] -> sum = 5

Edge cases:
- Flat ratings (all equal) → all get 1 candy.
- Strictly increasing or decreasing sequences → candies = [1..n] or [n..1] as appropriate.

"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Two-pass greedy solution (left->right then right->left).
        """
        if not ratings:
            return 0

        n = len(ratings)
        candies = [1] * n

        # Left-to-right pass: satisfy left neighbor condition
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right-to-left pass: satisfy right neighbor condition and preserve left pass using max
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1, 3, 2, 2, 1], 7),
        ([1, 1, 1, 1], 4),
        ([5, 4, 3, 2, 1], 15),  # strictly decreasing
    ]
    for ratings, expected in tests:
        out = sol.candy(ratings.copy())
        print(f"ratings={ratings} -> candies={out} (expected={expected})")
