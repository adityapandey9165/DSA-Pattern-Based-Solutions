"""
LeetCode: 155. Min Stack (Easy)
Problem link: https://leetcode.com/problems/min-stack/
Author: Aditya Pandey
Date: 2025-10-27

Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- push(val) — push element val onto the stack.
- pop() — removes the element on the top of the stack.
- top() — get the top element.
- getMin() — retrieve the minimum element in the stack.

Pattern: Stack (auxiliary stack for tracking minimums)

Approach:
1. Use two lists:
   - `stack` to store all pushed values (normal stack behavior).
   - `min` to store the current minima (monotonic stack of minima).
2. On `push(val)`:
   - Append val to `stack`.
   - If `min` is empty or `val <= min[-1]`, append val to `min`. (Use `<=` to correctly handle duplicates.)
3. On `pop()`:
   - Pop from `stack`. If the popped value equals `min[-1]`, also pop from `min`.
4. `top()` returns the last element of `stack`.
5. `getMin()` returns the last element of `min`.

Time Complexity: O(1) for all operations.
Space Complexity: O(n) worst case (when every pushed element becomes a new minimum).

Notes:
- Using `<=` when pushing to `min` ensures duplicate minima are tracked correctly, so popping one copy restores the previous minimum.
- The implementation assumes methods are called validly (e.g., no `top`/`getMin` on empty stack). You can add checks if you want defensive behavior.

"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min[-1]:
                self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())  # -3
    obj.pop()
    print(obj.top())     # 0
    print(obj.getMin())  # -2

    # test duplicates
    obj = MinStack()
    obj.push(2)
    obj.push(2)
    obj.push(1)
    obj.push(1)
    print(obj.getMin())  # 1
    obj.pop()            # pop 1
    print(obj.getMin())  # 1 (duplicate handled)
    obj.pop()            # pop 1
    print(obj.getMin())  # 2
