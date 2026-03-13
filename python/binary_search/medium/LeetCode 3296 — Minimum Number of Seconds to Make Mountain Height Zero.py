"""
LeetCode 3296 — Minimum Number of Seconds to Make Mountain Height Zero
Difficulty: Medium
Topic: Binary Search, Math

--------------------------------------------------

Problem
-------
You are given:

mountainHeight → total height to reduce to 0
workerTimes → list where workerTimes[i] is time needed
               for worker i to remove 1 unit initially.

Worker rule:
If worker time = w

1st unit  → w seconds
2nd unit → 2w seconds
3rd unit → 3w seconds
...

Total time for removing x units:

w * (1 + 2 + 3 + ... + x)
= w * x(x+1)/2

Goal:
Find minimum seconds required so all workers together
can remove mountainHeight.

--------------------------------------------------

Pattern
-------
Binary Search on Answer

We search the minimum time `t` such that workers
can remove ≥ mountainHeight.

For a worker with time w:

w * x(x+1)/2 ≤ t

Solve for x:

x(x+1)/2 ≤ t / w

x² + x - 2t/w ≤ 0

Using quadratic formula:

x = (-1 + sqrt(1 + 8t/w)) / 2

This gives how many units that worker can remove
within time t.

--------------------------------------------------

Algorithm
---------

1. Binary search time range
       left = 0
       right = 1e18

2. For each mid time
       calculate total units workers can remove

3. If total ≥ mountainHeight
       move right

4. Else
       move left

--------------------------------------------------

Time Complexity
---------------
Binary Search: log(1e18) ≈ 60

Each check: O(n)

Total:
O(n log T)

--------------------------------------------------

Space Complexity
----------------
O(1)

--------------------------------------------------
"""


from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        # check if workers can finish within time t
        def canfinish(t):

            total = 0

            for w in workerTimes:

                # solving quadratic
                v = (1 + (8 * t / w)) ** 0.5
                x = (v - 1) // 2

                total += x

                if total >= mountainHeight:
                    return True

            return total >= mountainHeight

        left = 0
        right = 10 ** 18

        while left < right:

            mid = (left + right) // 2

            if canfinish(mid):
                right = mid
            else:
                left = mid + 1

        return left


# -------------------------------
# Local Testing
# -------------------------------
if __name__ == "__main__":

    sol = Solution()

    mountainHeight = 4
    workerTimes = [2, 1, 1]

    print(sol.minNumberOfSeconds(mountainHeight, workerTimes))
