"""
LeetCode: 102. Binary Tree Level Order Traversal (Medium)
Problem link: https://leetcode.com/problems/binary-tree-level-order-traversal/
Author: Aditya Pandey
Date: 2025-09-08

Problem:
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(Level by level, left to right).

Pattern: BFS / Queue — Level Order Traversal

Approach:
- Use a queue to perform BFS.
- Initialize the queue with root.
- While the queue is not empty:
    - For each node in current level (len(queue) nodes):
        - Pop node, append its value to current level list.
        - Add its children (left and right) to the queue.
    - Append the current level list to result.
- Return result list of lists.

Time Complexity: O(n) — visit each node once.
Space Complexity: O(n) — queue may hold up to all nodes in a level.

Common Mistakes:
- Forgetting to check if root is None.
- Mixing up node.left and node.right insertions.
- Modifying the queue while iterating without fixing the level length.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res
