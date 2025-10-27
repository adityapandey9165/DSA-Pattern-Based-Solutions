"""
LeetCode: 150. Evaluate Reverse Polish Notation (Medium)
Problem link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Author: Aditya Pandey
Date: 2025-10-27

Problem:
You are given an array of strings `tokens` representing an arithmetic expression 
in Reverse Polish Notation (RPN).

Evaluate the expression and return an integer that represents the value.

Notes:
- Valid operators are '+', '-', '*', '/'.
- Each operand may be an integer or another expression.
- Division between two integers truncates toward zero.
- No division by zero.
- The input represents a valid arithmetic expression in RPN.
- All intermediate results fit in a 32-bit integer.

Pattern: Stack-based Expression Evaluation

Approach:
1. Initialize an empty stack.
2. Traverse each token:
   - If token is a number → push to stack.
   - If token is an operator → pop top two elements (b, a),
     compute `a op b`, and push the result back.
3. Use `int(a / b)` for division to ensure truncation toward zero.
4. Final result is the only element left in the stack.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:  # '/'
                    stack.append(int(a / b))  # truncates toward zero
            else:
                stack.append(int(token))

        return stack[0]


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["2","1","+","3","*"]))  # 9
    print(sol.evalRPN(["4","13","5","/","+"]))  # 6
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22
