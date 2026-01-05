"""
LeetCode: 1975. Maximum Matrix Sum (Medium)
Problem link: https://leetcode.com/problems/maximum-matrix-sum/
Author: Aditya Pandey
Date: 2025-12-30

Problem:
You are given an integer matrix.
You can change the sign of any element any number of times.

Return the **maximum possible sum** of the matrix after performing any number
of sign-flip operations.

---

Approach: Greedy + Math Observation

Key observations:
1. Flipping signs does not change the absolute value of elements.
2. To maximize the sum, we want **all values to be positive**.
3. If the count of negative numbers is even:
   - We can flip signs to make all numbers positive.
4. If the count of negative numbers is odd:
   - One element must remain negative.
   - To minimize loss, keep the **smallest absolute value** negative.

Steps:
1. Count the number of negative elements.
2. Track the minimum absolute value in the matrix.
3. Add the absolute value of all elements.
4. If negative count is odd, subtract twice the minimum absolute value.

---

Why subtract 2 × minAbs?
- We initially added all absolute values.
- One element must remain negative → reduce sum by 2 × |min|.

---

Time Complexity:
- O(m × n)

Space Complexity:
- O(1)
"""


from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_count = 0
        min_abs = float("inf")
        total_sum = 0

        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                min_abs = min(min_abs, abs(val))
                total_sum += abs(val)

        # If odd number of negatives, one smallest abs value stays negative
        if neg_count % 2 == 1:
            return total_sum - 2 * min_abs

        return total_sum


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.maxMatrixSum([[1, -1], [-1, 1]]))
    # Expected: 4

    print(sol.maxMatrixSum([[1, 2, 3], [-1, -2, -3]]))
    # Expected: 12

    print(sol.maxMatrixSum([[-1]]))
    # Expected: -1
