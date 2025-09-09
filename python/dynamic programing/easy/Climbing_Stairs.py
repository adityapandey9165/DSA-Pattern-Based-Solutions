"""
LeetCode: 70. Climbing Stairs (Easy)
Problem link: https://leetcode.com/problems/climbing-stairs/
Author: Aditya Pandey
Date: 2025-09-08

Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can climb either 1 or 2 steps.
In how many distinct ways can you climb to the top?

---

Approach 1: Top-Down DP (Memoization)
- Define dfs(i) as the number of ways to reach the top starting from step i.
- Recurrence:
    - If i == n → 1 way (reached top).
    - If i > n → 0 ways (invalid).
    - Otherwise: dfs(i) = dfs(i+1) + dfs(i+2)
- Use memoization (dictionary dp) to cache results and avoid recomputation.
- Time: O(n), Space: O(n) (recursion + memo).

Approach 2: Bottom-Up DP
- dp[i] = number of ways to reach step i.
- Transition: dp[i] = dp[i-1] + dp[i-2]
- Base cases: dp[0] = 1, dp[1] = 1
- Answer = dp[n].
- Time: O(n), Space: O(n)

Approach 3: Fibonacci Optimization
- This problem reduces to Fibonacci: ways(n) = ways(n-1) + ways(n-2)
- Can compute iteratively with two variables.
- Time: O(n), Space: O(1).

Pattern:
- Classic DP "staircase / step choices" problem.
- Generalized to "how many ways to climb if you can take 1..k steps?".
- Equivalent to Fibonacci sequence.

Common Interview Questions:
1. Can you implement the bottom-up DP version?
2. How to reduce space from O(n) to O(1)?
3. What if you can climb 1, 2, or 3 steps? (Generalization)
4. What if steps array is given (e.g., [1,3,5]) instead of fixed 1,2?
5. Compare recursion + memo vs iterative DP performance.

Example:
Input: n = 3
Paths: (1+1+1), (1+2), (2+1) → 3 ways
Output: 3
"""

from typing import Dict

# --- Approach 1: Top-Down Memoization ---
class SolutionMemo:
    def climbStairs(self, n: int) -> int:
        dp: Dict[int, int] = {}

        def dfs(i: int) -> int:
            if i == n: 
                return 1
            if i > n: 
                return 0
            if i in dp: 
                return dp[i]
            dp[i] = dfs(i + 1) + dfs(i + 2)
            return dp[i]

        return dfs(0)


# --- Approach 2: Bottom-Up DP ---
class SolutionDP:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# --- Approach 3: Fibonacci (Optimized) ---
class SolutionFib:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        prev1, prev2 = 1, 2
        for _ in range(3, n + 1):
            prev1, prev2 = prev2, prev1 + prev2
        return prev2


if __name__ == "__main__":
    sol = SolutionMemo()
    print(sol.climbStairs(3))  # expected: 3
    print(sol.climbStairs(5))  # expected: 8
