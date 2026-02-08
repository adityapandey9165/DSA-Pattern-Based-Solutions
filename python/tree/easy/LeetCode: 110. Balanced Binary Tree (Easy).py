"""
LeetCode: 110. Balanced Binary Tree (Easy)
Problem link: https://leetcode.com/problems/balanced-binary-tree/
Author: Aditya Pandey
Date: 2026-02-08

------------------------------------------------------------
Problem:
Given a binary tree, determine if it is height-balanced.

A binary tree is balanced if for every node, the heights of the left and
right subtrees differ by at most 1.

------------------------------------------------------------
Pattern:
Tree DFS / Post-order (Bottom-up)

------------------------------------------------------------
Core Insight:
Instead of recomputing subtree heights again and again (top-down),
we compute height bottom-up and return -1 immediately if a subtree
is unbalanced. This avoids redundant work.

------------------------------------------------------------
Approaches:
1) Top-down (Brute Force)
   - For each node, compute heights separately.
   - Time: O(n²) worst-case (skewed tree)

2) Bottom-up (Optimal) ✅
   - Post-order DFS
   - Propagate height or -1 if unbalanced
   - Time: O(n)

------------------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(h)  (recursion stack)
------------------------------------------------------------
"""

from typing import Optional, List
from collections import deque


# -----------------------
# Definition for a binary tree node
# -----------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -----------------------
# Solution (Optimal)
# -----------------------
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Bottom-up DFS.
        Returns True if tree is balanced, else False.
        """
        def height(node):
            if not node:
                return 0

            left_h = height(node.left)
            if left_h == -1:
                return -1

            right_h = height(node.right)
            if right_h == -1:
                return -1

            if abs(left_h - right_h) > 1:
                return -1

            return 1 + max(left_h, right_h)

        return height(root) != -1


# ------------------------------------------------------------
# Building Tree FROM SCRATCH (Interview / Local Testing)
# ------------------------------------------------------------
def buildTreeFromArray(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build binary tree from level-order array representation.
    None represents missing nodes.

    Example:
    arr = [3, 9, 20, None, None, 15, 7]

            3
           / \
          9  20
             / \
            15  7
    """
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root


# -----------------------
# Example Usage (Scratch → Tree → Solution)
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Balanced Tree
    arr1 = [3, 9, 20, None, None, 15, 7]
    root1 = buildTreeFromArray(arr1)
    print("Balanced Tree:", sol.isBalanced(root1))  # True

    # Example 2: Unbalanced Tree
    arr2 = [1, 2, None, 3]
    root2 = buildTreeFromArray(arr2)
    print("Unbalanced Tree:", sol.isBalanced(root2))  # False

    # Example 3: Empty Tree
    arr3 = []
    root3 = buildTreeFromArray(arr3)
    print("Empty Tree:", sol.isBalanced(root3))  # True


"""
Things interviewers often miss / ask:
- Why top-down is inefficient? (Repeated height computation)
- How early stopping helps performance
- How to construct tree from array input
- Why empty tree is balanced
- Difference between recursion depth and node count

------------------------------------------------------------
