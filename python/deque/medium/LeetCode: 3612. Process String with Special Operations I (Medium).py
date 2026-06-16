"""
LeetCode: 3612. Process String with Special Operations I (Medium)
Problem Link: https://leetcode.com/problems/process-string-with-special-operations-i/
Author: Aditya Pandey
Date: 2026-06-16

------------------------------------------------------------
Problem:
You are given a string s containing:
- lowercase letters ('a' to 'z')
- '*'  -> delete one character
- '#'  -> duplicate the current string
- '%'  -> reverse the current string

Process the string from left to right and return the final string.

------------------------------------------------------------
Pattern:
Deque Simulation + Lazy Reversal

------------------------------------------------------------
Approach:
We use a deque to support efficient operations at both ends.

Instead of physically reversing the string every time we see '%',
we maintain a boolean flag:
- is_reverse = False  -> normal orientation
- is_reverse = True   -> reversed orientation

Rules:
1. Lowercase letter:
   - normal mode   -> append to right
   - reverse mode  -> append to left

2. '*':
   - delete from the logical end
   - normal mode   -> pop from right
   - reverse mode  -> pop from left

3. '#':
   - duplicate the current string
   - this is expensive because the string size doubles
   - we copy the current deque and append it to itself

4. '%':
   - just toggle the direction flag
   - no physical reversal here

At the end:
- if is_reverse is still True, reverse the deque once

------------------------------------------------------------
Why this works:
The deque always stores the current characters in the order that
matches the active orientation.

The reverse flag tells us which side is the logical front/back.
This avoids repeated full-string reversals.

------------------------------------------------------------
Brute Force Idea:
A brute force solution would rebuild the string every time:
- reverse on '%'
- delete by slicing on '*'
- duplicate by concatenation on '#'

This is easy to understand but too slow.

Time Complexity:
- Letter / '*' / '%' operations: O(1)
- '#' operation: O(current length) because we must duplicate the string

Overall worst case:
O(n^2)

Space Complexity:
O(n)

------------------------------------------------------------
Things to Pay Attention To:
- Do not reverse the entire string on every '%'
- '*' should delete from the logical end
- '#' duplicates the current content, so it can be expensive
- If the final orientation is reversed, reverse the deque before returning
- Empty deque must be handled safely for '*'

------------------------------------------------------------
Common Mistakes:
- Using string concatenation repeatedly
- Physically reversing the string every time '%'
- Wrong side deletion in reverse mode
- Forgetting that duplication can make runtime quadratic
------------------------------------------------------------
"""

from collections import deque


class Solution:
    def processStr(self, s: str) -> str:
        res = deque()
        is_reverse = False

        for ch in s:
            # lowercase letter
            if 'a' <= ch <= 'z':
                if not is_reverse:
                    res.append(ch)
                else:
                    res.appendleft(ch)

            # delete one character from the logical end
            elif ch == '*':
                if res:
                    if not is_reverse:
                        res.pop()
                    else:
                        res.popleft()

            # duplicate current string
            elif ch == '#':
                if res:
                    snapshot = list(res)
                    # duplicate the current deque content
                    res.extend(snapshot)

            # reverse current string logically
            else:  # '%'
                is_reverse = not is_reverse

        # If still reversed, convert back to normal orientation
        if is_reverse:
            res.reverse()

        return "".join(res)


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.processStr("abc"))      # Expected: abc
    print(sol.processStr("ab#"))      # Expected: abab
    print(sol.processStr("ab%c"))     # Expected depends on operation rules
    print(sol.processStr("a*b"))      # Expected: b
