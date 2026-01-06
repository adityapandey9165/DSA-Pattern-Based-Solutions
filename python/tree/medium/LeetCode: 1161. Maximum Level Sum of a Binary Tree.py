"""
LeetCode: 1161. Maximum Level Sum of a Binary Tree (Medium)
Problem link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
Author: Aditya Pandey
Date: 2025-12-30

Problem:
Given the root of a binary tree, return the **level number (1-indexed)**
that has the maximum sum of node values.

If there are multiple levels with the same maximum sum,
return the **smallest level number**.

---

Approach: Breadth-First Search (Level Order Traversal)

We traverse the tree level by level using BFS:
1. Use a queue to process nodes level by level.
2. For each level:
   - Compute the sum of node values.
   - Store the sum in a list.
3. After traversal, find the level with the maximum sum.
4. Return the smallest level index (1-based) having the maximum sum.

---

Why BFS?
- Each tree level is processed independently.
- BFS naturally aligns with level-order traversal.
- Guarantees correct ordering for level indexing.

---

Time Complexity:
- O(n), where n is the number of nodes

Space Complexity:
- O(n) for the queue in the worst case
"""


from typing import Optional
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level_sums = []

        while q:
            next_level = deque()
            level_sum = 0

            while q:
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level_sums.append(level_sum)
            q = next_level

        max_sum = level_sums[0]
        answer = 1

        for i, val in enumerate(level_sums):
            if val > max_sum:
                max_sum = val
                answer = i + 1

        return answer


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    # Example tree:
    #        1
    #       / \
    #      7   0
    #     / \
    #    7  -8
    #
    # Level sums: [1, 7, -1]
    # Expected answer: 2

    root = TreeNode(
        1,
        TreeNode(7, TreeNode(7), TreeNode(-8)),
        TreeNode(0)
    )

    sol = Solution()
    print(sol.maxLevelSum(root))  # Expected: 2
