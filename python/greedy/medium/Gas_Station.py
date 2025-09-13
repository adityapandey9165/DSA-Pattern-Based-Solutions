"""
LeetCode: 134. Gas Station (Medium)
Problem link: https://leetcode.com/problems/gas-station/
Author: Aditya Pandey
Date: 2025-09-13

Problem:
There are n gas stations along a circular route. The amount of gas at station i is gas[i],
and it costs cost[i] gas to travel from station i to station (i+1) mod n.
Return the index of the starting gas station if you can travel around the circuit once in the clockwise direction, or -1 if you cannot.
If a solution exists, it is guaranteed to be unique.

Pattern: Greedy (One-pass) — Maintain running tank and reset start when tank goes negative

Approach (Intuition + Algorithm):
1. If total gas < total cost, it is impossible to complete the circuit → return -1.
2. Otherwise, there must be exactly one valid start index. We can find it in one pass:
   - Maintain three variables:
     • total_gas  = sum of gas seen so far (global)
     • total_cost = sum of cost seen so far (global)
     • tank       = running balance from current candidate start
     • start      = candidate starting index
   - Iterate i from 0 to n-1:
       tank += gas[i] - cost[i]
       if tank < 0:
           # cannot start from current `start` (or any index between start and i)
           start = i + 1   # try next index as new start
           tank = 0        # reset running balance
   - After the loop, if total_gas >= total_cost return start else -1.

Why resetting start works (short proof sketch):
- If starting at `start` we fail at index `i` (tank < 0), then any index `j` in [start, i] cannot be a valid start:
  from `j` you would have even less gas when reaching `i` (you skipped some positive contributions), so you would also fail. Thus it's safe to skip the whole range and set start = i+1.
- Combined with the global total check (total_gas >= total_cost), the found `start` is guaranteed to complete the circuit.

Time Complexity: O(n) — single pass
Space Complexity: O(1) — constant extra space

Common Mistakes:
- Forgetting the `total_gas >= total_cost` check (leads to wrong positives).
- Resetting start but not resetting tank to 0.
- Using brute-force trying every start (O(n^2)) which TLEs for large n.
- Off-by-one errors in start assignment when tank < 0.

Example Walkthrough:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
n = 5
total_gas = 15, total_cost = 15 -> possible

i=0: tank = 1-3 = -2  -> tank<0 -> start=1, tank=0
i=1: tank = 2-4 = -2  -> tank<0 -> start=2, tank=0
i=2: tank = 3-5 = -2  -> tank<0 -> start=3, tank=0
i=3: tank = 4-1 = 3   -> continue
i=4: tank = 3 + (5-2) = 6
end -> total_gas >= total_cost -> return start = 3

Result: 3 (starting at station index 3 works)

Alternate approaches:
- Brute-force: Try every start, simulate travel (O(n^2)). Use only for small inputs or explanation.
- Prefix-sum / two-pointer variants exist but the greedy one-pass is simplest and optimal.

"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Return the starting gas station index to complete the circuit, or -1 if impossible.
        """
        total_gas = total_cost = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

            # If tank is negative, cannot start from `start`..`i`, so try i+1
            if tank < 0:
                start = i + 1
                tank = 0

        return start if total_gas >= total_cost else -1


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1,2,3,4,5], [3,4,5,1,2], 3),
        ([2,3,4], [3,4,3], -1),
        ([5,1,2,3,4], [4,4,1,5,1], 4),
        ([1], [1], 0),
    ]

    for gas, cost, expected in tests:
        out = sol.canCompleteCircuit(gas.copy(), cost.copy())
        print(f"gas={gas}, cost={cost} -> start={out} (expected={expected})")
