"""
LeetCode: 799. Champagne Tower (Medium)
Problem Link: https://leetcode.com/problems/champagne-tower/
Author: Aditya Pandey
Date: 2026-02-14

Problem:
We stack glasses in a pyramid: the top row has 1 glass, the next row has 2, and so on.
When you pour `poured` cups into the top glass, any amount above 1 cup overflows
equally to the two glasses immediately below (left and right). Each glass holds at most 1 cup.

Return how full the glass at `query_row` and `query_glass` is (a value in [0,1]).

Example:
Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.5

------------------------------------------------------------
Pattern:
Dynamic Programming / Simulation (Row-by-row propagation)

------------------------------------------------------------
How this solution works (step-by-step):

1. DP interpretation:
   - Let dp[r][c] represent the amount of champagne in the glass at row r, column c
     after pouring and all propagation up to row r has occurred.
   - We set dp[0][0] = poured (top glass receives all poured amount).

2. Propagation (simulation):
   - Iterate rows from 0 to query_row - 1.
   - For each glass dp[r][c], compute overflow = max(0.0, dp[r][c] - 1).
   - The overflow is split equally: overflow/2 goes to dp[r+1][c] and dp[r+1][c+1].
   - After processing row r, dp[r][c] effectively becomes min(1, dp[r][c]) but we don't need
     to clamp until the end — we only carry overflow downward.

3. Final answer:
   - The glass at dp[query_row][query_glass] may contain more than 1 due to
     propagation; return min(1.0, dp[query_row][query_glass]).

------------------------------------------------------------
Why this is correct:
- The process is literally the physical pouring process: overflow at each glass only depends
  on what poured into that glass (which is known after processing previous rows).
- We simulate level-by-level so that overflows from row r are available for row r+1.

------------------------------------------------------------
Optimizations:
- Space optimized: We only need the current row and the next row (two arrays), or even one
  array updated right-to-left per row. This reduces space from O(query_row^2) to O(query_row).
- Early stopping: If all entries in a row are <= 1 and no overflow exists, further propagation
  will do nothing — but typically the row-by-row loop is cheap for query_row up to ~100.

------------------------------------------------------------
Time Complexity:
- O(query_row^2) in the worst case (we fill a triangle of size ~query_row*(query_row+1)/2).
  In practice query_row ≤ 100 (LeetCode constraints), so this is fine.

Space Complexity:
- O(query_row^2) for the full DP table implementation below.
- O(query_row) if using the space-optimized one-dimensional approach.

------------------------------------------------------------
Common pitfalls:
- Forgetting to use `max(0.0, dp[r][c] - 1)` — negative overflow should not be propagated.
- Off-by-one in loop bounds for rows/columns.
- Returning dp[query_row][query_glass] without clamping to 1.0.
- Using an array that’s too small for `query_row` (need row length = r+1 for row r).

------------------------------------------------------------
"""

from typing import List


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Build DP triangle up to query_row
        dp = [[0.0] * (r + 1) for r in range(query_row + 1)]
        dp[0][0] = float(poured)

        for r in range(query_row):
            for c in range(len(dp[r])):
                overflow = max(0.0, dp[r][c] - 1.0)
                if overflow > 0:
                    dp[r + 1][c] += overflow / 2.0
                    dp[r + 1][c + 1] += overflow / 2.0

        return min(1.0, dp[query_row][query_glass])


# -----------------------
# Space-optimized variant (optional)
# -----------------------
def champagneTower_space_opt(poured: int, query_row: int, query_glass: int) -> float:
    """
    Uses a single list of length query_row+1, updated in reverse to avoid
    overwriting values needed for the current row's computation.
    """
    row = [0.0] * (query_row + 1)
    row[0] = float(poured)

    for r in range(1, query_row + 1):
        # update from right to left so we don't overwrite values needed for next calculation
        for c in range(r, -1, -1):
            left = row[c - 1] if c - 1 >= 0 else 0.0
            right = row[c] if c < r else 0.0
            # compute overflow contribution from previous row's glasses
            overflow = 0.0
            if c - 1 >= 0:
                overflow += max(0.0, left - 1.0) / 2.0
            if c < r:
                overflow += max(0.0, right - 1.0) / 2.0
            row[c] = overflow

    return min(1.0, row[query_glass])


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    cases = [
        (1, 0, 0, 1.0),
        (2, 1, 1, 0.5),
        (100000009, 33, 17, 1.0),  # large poured will fill many rows (clamped)
        (4, 2, 1, 0.5),
    ]

    print("DP (triangle) results:")
    for poured, qr, qg, expected in cases:
        out = sol.champagneTower(poured, qr, qg)
        print(f"poured={poured}, row={qr}, glass={qg} -> {out} (expected approx {expected})")

    print("\nSpace-optimized results:")
    for poured, qr, qg, expected in cases:
        out = champagneTower_space_opt(poured, qr, qg)
        print(f"poured={poured}, row={qr}, glass={qg} -> {out} (expected approx {expected})")


