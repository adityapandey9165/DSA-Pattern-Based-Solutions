"""
LeetCode: 2751. Robot Collisions (Hard)
Problem Link: https://leetcode.com/problems/robot-collisions/
Author: Aditya Pandey
Date: 2026-04-02

------------------------------------------------------------
Problem:
You are given:
- positions[i]  -> starting position of robot i
- healths[i]    -> health of robot i
- directions    -> 'L' or 'R' for each robot

All robots move at the same speed.

Rules:
- When two robots collide:
  - The robot with smaller health is removed
  - The robot with larger health loses 1 health
  - If both healths are equal, both are removed

Return the healths of the surviving robots in the original order.

------------------------------------------------------------
Pattern:
Sorting + Stack Simulation

------------------------------------------------------------
Why sorting is needed:
Robots only collide based on their position order.
So we sort by position first, then simulate collisions from left to right.

------------------------------------------------------------
Brute Force Idea:
Sort robots by position and repeatedly scan the list.
Whenever we find an adjacent pair:
- left robot moving Right
- right robot moving Left

we resolve the collision and restart the scan.

This is easy to understand but inefficient.

Time Complexity:
O(n^2) in the worst case

------------------------------------------------------------
Optimal Approach:
Use a stack to store robots moving Right.

When a Left-moving robot appears:
- It can only collide with robots in the stack
- Resolve collisions one by one from the top of the stack

This works because:
- A right-moving robot can only collide with a robot coming from the right
- The stack keeps the most recent possible collision candidate

Time Complexity:
O(n log n) because of sorting
Stack simulation itself is O(n)

Space Complexity:
O(n)

------------------------------------------------------------
Things to Pay Attention To:
- Always sort by position first
- Only right-moving robots go into the stack
- Handle three cases carefully:
  1. current health < stack top health
  2. current health > stack top health
  3. equal health
- Return survivors in original order
- Update health after each collision correctly

------------------------------------------------------------
"""


from typing import List


class Solution:
    # ------------------------------------------------------------
    # Brute Force (educational, not recommended)
    # ------------------------------------------------------------
    def survivedRobotsHealths_bruteforce(
        self,
        positions: List[int],
        healths: List[int],
        directions: str
    ) -> List[int]:
        """
        Repeatedly scan adjacent robots in sorted order and resolve the
        first possible collision until no collisions remain.

        This is simple to understand, but can be O(n^2) or worse in practice.
        """
        robots = sorted([
            [positions[i], healths[i], directions[i], i]
            for i in range(len(positions))
        ])

        n = len(robots)
        alive = [True] * n
        hp = [r[1] for r in robots]

        changed = True
        while changed:
            changed = False
            for i in range(n - 1):
                if not alive[i] or not alive[i + 1]:
                    continue

                pos1, h1, d1, idx1 = robots[i]
                pos2, h2, d2, idx2 = robots[i + 1]

                # Only adjacent R-L pair can collide
                if d1 == 'R' and d2 == 'L':
                    changed = True

                    if hp[i] > hp[i + 1]:
                        hp[i] -= 1
                        alive[i + 1] = False
                    elif hp[i] < hp[i + 1]:
                        hp[i + 1] -= 1
                        alive[i] = False
                    else:
                        alive[i] = False
                        alive[i + 1] = False

                    # restart scanning after one collision
                    break

        result = []
        for i in range(n):
            if alive[i]:
                result.append((robots[i][3], hp[i]))

        result.sort()
        return [h for _, h in result]

    # ------------------------------------------------------------
    # Optimal Solution
    # ------------------------------------------------------------
    def survivedRobotsHealths(
        self,
        positions: List[int],
        healths: List[int],
        directions: str
    ) -> List[int]:

        # Sort robots by position
        robots = sorted([
            [positions[i], healths[i], directions[i], i]
            for i in range(len(positions))
        ])

        stack = []  # indices of robots moving right
        alive = [True] * len(robots)

        for i in range(len(robots)):
            pos, hel, direc, idx = robots[i]

            if direc == 'R':
                stack.append(i)
            else:
                # current robot moving left may collide with previous right-moving robots
                while stack and hel > 0:
                    j = stack[-1]
                    _, right_hel, _, _ = robots[j]

                    if hel < right_hel:
                        # left robot dies, right robot loses 1 health
                        alive[i] = False
                        robots[j][1] -= 1
                        hel = 0

                    elif hel > right_hel:
                        # right robot dies, left robot loses 1 health and continues
                        stack.pop()
                        alive[j] = False
                        hel -= 1

                    else:
                        # both die
                        stack.pop()
                        alive[j] = False
                        alive[i] = False
                        hel = 0

                robots[i][1] = hel

        # collect surviving robots in original order
        result = []
        for i in range(len(robots)):
            if alive[i]:
                result.append((robots[i][3], robots[i][1]))

        result.sort()
        return [h for _, h in result]


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.survivedRobotsHealths(
        [3, 5, 2, 6],
        [10, 10, 15, 12],
        "RLRL"
    ))
    # Expected: [14]

    print(sol.survivedRobotsHealths(
        [1, 2, 5, 6],
        [10, 10, 11, 11],
        "RLRL"
    ))
    # Expected survivors depend on collision chain

    print(sol.survivedRobotsHealths_bruteforce(
        [3, 5, 2, 6],
        [10, 10, 15, 12],
        "RLRL"
    ))
