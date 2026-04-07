"""
LeetCode: 2069. Walking Robot Simulation II (Medium)
Problem Link: https://leetcode.com/problems/walking-robot-simulation-ii/
Author: Aditya Pandey
Date: 2026-04-06

------------------------------------------------------------
Problem:
A robot is placed on a grid of size width x height.

- Starts at (0,0) facing East
- Moves along the perimeter only (edges of grid)

Operations:
1. step(num) → move num steps along perimeter
2. getPos() → return current position
3. getDir() → return current direction

------------------------------------------------------------
Pattern:
Simulation + Math Optimization (Perimeter Cycle)

------------------------------------------------------------
Key Insight:
Robot only moves along the boundary.

Total perimeter steps:
perimeter = 2 * (width + height - 2)

So instead of simulating every step:
→ Reduce steps using modulo

num %= perimeter

------------------------------------------------------------
Approach:
1. Store:
   - current position (x, y)
   - current direction index

2. Directions:
   0 → North
   1 → East
   2 → South
   3 → West

3. Movement:
   - Try moving in current direction
   - If boundary reached:
       → move to boundary
       → reduce remaining steps
       → change direction (turn clockwise)

------------------------------------------------------------
Edge Case (VERY IMPORTANT ⚠️):
If num % perimeter == 0:
→ robot completes full cycle
→ position becomes same BUT direction changes

Fix:
    if num == 0:
        num = perimeter

------------------------------------------------------------
Time Complexity:
step(): O(1) amortized
(At most 4 direction changes per call)

getPos(): O(1)
getDir(): O(1)

------------------------------------------------------------
Space Complexity:
O(1)

------------------------------------------------------------
Things to Remember:
- Always use modulo to avoid TLE
- Handle full cycle case (num == 0)
- Direction update:
      clockwise → (d + 3) % 4   (based on this implementation)
- Robot moves ONLY on edges

------------------------------------------------------------
Common Mistakes:
- Forgetting modulo → TLE
- Wrong direction update
- Not handling full cycle case
- Thinking robot moves inside grid (it doesn't)

------------------------------------------------------------
"""


from typing import List


class Robot:

    def __init__(self, width: int, height: int):

        self.curr = [0, 0]

        # Directions: North, East, South, West
        self.dirr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        self.d = 1  # Start facing East
        self.width = width
        self.height = height

    def step(self, num: int) -> None:

        perimeter = 2 * (self.width + self.height - 2)

        num %= perimeter
        if num == 0:
            num = perimeter

        while True:
            dx, dy = self.dirr[self.d]
            x, y = self.curr

            # Moving right (East)
            if dx > 0:
                p = x + num
                if p < self.width:
                    x = p
                    self.curr = [x, y]
                    return
                else:
                    num -= (self.width - x - 1)
                    x = self.width - 1
                    self.curr = [x, y]
                    self.d = (self.d + 3) % 4
                    continue

            # Moving left (West)
            elif dx < 0:
                p = x - num
                if p >= 0:
                    x = p
                    self.curr = [x, y]
                    return
                else:
                    num -= x
                    x = 0
                    self.curr = [x, y]
                    self.d = (self.d + 3) % 4
                    continue

            # Moving up (North)
            if dy > 0:
                p = y + num
                if p < self.height:
                    y = p
                    self.curr = [x, y]
                    return
                else:
                    num -= (self.height - y - 1)
                    y = self.height - 1
                    self.curr = [x, y]
                    self.d = (self.d + 3) % 4
                    continue

            # Moving down (South)
            elif dy < 0:
                p = y - num
                if p >= 0:
                    y = p
                    self.curr = [x, y]
                    return
                else:
                    num -= y
                    y = 0
                    self.curr = [x, y]
                    self.d = (self.d + 3) % 4
                    continue

    def getPos(self) -> List[int]:
        return self.curr

    def getDir(self) -> str:
        direc = ["North", "East", "South", "West"]
        return direc[self.d]


# -----------------------
# Quick tests
# -----------------------
if __name__ == "__main__":
    robot = Robot(6, 3)

    robot.step(2)
    print(robot.getPos(), robot.getDir())  # [2,0], East

    robot.step(2)
    print(robot.getPos(), robot.getDir())  # [4,0], East

    robot.step(2)
    print(robot.getPos(), robot.getDir())  # [5,1], North

    robot.step(100)
    print(robot.getPos(), robot.getDir())  # cycle handled
