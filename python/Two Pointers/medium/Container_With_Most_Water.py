"""
LeetCode: 11. Container With Most Water (Medium)
Problem link: https://leetcode.com/problems/container-with-most-water/
Author: Aditya Pandey
Date: 2025-09-08

Problem:
Given n non-negative integers `height` representing vertical lines on x-axis, 
find two lines that together with x-axis form a container, such that it contains 
the most water. Return the maximum area.

Pattern: Two Pointers — Greedy Optimization

Approach:
- Use two pointers, `left` at 0 and `right` at len(height)-1.
- Compute area = min(height[left], height[right]) * (right - left).
- Move the pointer pointing to the shorter line inward (since moving taller line won't increase area).
- Update max_area if current area is greater.
- Repeat until left >= right.

Time Complexity: O(n) — single pass through array.
Space Complexity: O(1) — constant space.

Common Mistakes:
- Trying to check all pairs (O(n^2)) — inefficient.
- Not updating pointers correctly (must move the smaller height line).
- Confusing width vs. height in area calculation.

Example Walkthrough:
height = [1,8,6,2,5,4,8,3,7]
left=0, right=8 -> area = min(1,7)*(8-0)=8 -> max_area=8
height[left]<height[right] -> move left=1
left=1, right=8 -> area=min(8,7)*(8-1)=49 -> max_area=49
...
Continue until left>=right -> final max_area=49
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            curr_area = min(height[left], height[right]) * width
            max_area = max(max_area, curr_area)
            
            # Move the pointer with smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


if __name__ == "__main__":
    # Quick tests for revision
    sol = Solution()
    
    heights1 = [1,8,6,2,5,4,8,3,7]
    print("Max area:", sol.maxArea(heights1))  # Expected: 49
    
    heights2 = [1,1]
    print("Max area:", sol.maxArea(heights2))  # Expected: 1
    
    heights3 = [4,3,2,1,4]
    print("Max area:", sol.maxArea(heights3))  # Expected: 16
