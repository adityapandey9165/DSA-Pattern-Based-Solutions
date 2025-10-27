"""
LeetCode: 20. Valid Parentheses (Easy)
Problem link: https://leetcode.com/problems/valid-parentheses/
Author: Aditya Pandey
Date: 2025-10-27

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.

Pattern: Stack (LIFO)

Approach:
- Use a stack to track opening brackets.
- When a closing bracket is seen, check whether the stack top matches the corresponding opening bracket.
- If it matches, pop the stack; otherwise the string is invalid.
- In the end, the stack must be empty for the string to be valid.

Time Complexity: O(n) — one pass through the string.
Space Complexity: O(n) — stack holds at most n characters.
"""

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cond_map = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            # if ch is a closing bracket and top of stack matches its opening
            if stack and ch in cond_map and cond_map[ch] == stack[-1]:
                stack.pop()
            else:
                # push opening brackets or unmatched closing brackets
                stack.append(ch)

        return stack == []


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))        # True
    print(sol.isValid("()[]{}"))    # True
    print(sol.isValid("(]"))        # False
    print(sol.isValid("([)]"))      # False
    print(sol.isValid("{[]}"))      # True
