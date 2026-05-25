"""
LeetCode: 1871. Jump Game VII (Medium)
Problem Link: https://leetcode.com/problems/jump-game-vii/
Author: Aditya Pandey
Date: 2026-05-20

------------------------------------------------------------
Problem:
You are given a binary string s and two integers minJump and maxJump.

You start at index 0 and want to reach index n - 1.

Rules:
- You can jump from index i to any index j such that:
    i + minJump <= j <= i + maxJump
- You can only land on positions where s[j] == '0'

Return True if you can reach the last index, otherwise False.

------------------------------------------------------------
Pattern:
BFS / Sliding Window Optimization

------------------------------------------------------------
Approach:
We use BFS to explore reachable positions.

At each index i:
- All valid next positions are in the range:
      [i + minJump, i + maxJump]

To avoid checking the same range again and again:
- keep track of the farthest index already processed
- only scan new indices once

This makes the solution efficient.

------------------------------------------------------------
Why this works:
BFS explores reachable states level by level.
A position is only useful if it is reachable from a valid previous index.
Using `farthest` prevents repeated scanning of the same range,
which is the key optimization.

------------------------------------------------------------
Time Complexity:
O(n)

Each index is processed at most once.

------------------------------------------------------------
Space Complexity:
O(n)

Used for the visited array and queue.

------------------------------------------------------------
Things to Pay Attention To:
- Start from index 0 only if s[0] == '0'
- Do not scan already-processed indices again
- Only land on positions with '0'
- Return True immediately when reaching n - 1
- `farthest` is important for avoiding TLE

------------------------------------------------------------
Common Mistakes:
- Rechecking the same jump range multiple times
- Forgetting to mark visited
- Not handling the last index early
- Using naive BFS without range optimization
------------------------------------------------------------
"""

from collections import deque
from typing import List


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        # Start must be reachable
        if s[0] != '0':
            return False

        vis = [False] * n
        vis[0] = True

        q = deque([0])
        farthest = 0  # farthest index already processed in jump ranges

        while q:
            i = q.popleft()

            if i == n - 1:
                return True

            # Only scan indices not already processed
            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):
                if s[j] == '0' and not vis[j]:
                    vis[j] = True
                    q.append(j)

            # Mark range as processed
            farthest = max(farthest, end)

        return False


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.canReach("011010", 2, 3))   # Expected: True
    print(sol.canReach("01101110", 2, 3))  # Expected: False
    print(sol.canReach("0000000", 2, 5))   # Expected: True
