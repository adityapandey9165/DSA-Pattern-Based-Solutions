"""
LeetCode: 865. Smallest Subtree with all the Deepest Nodes (Medium)
Problem link: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
Author: Aditya Pandey
Date: 2025-12-30

Problem:
Given the root of a binary tree, return the smallest subtree that contains
all the deepest nodes in the tree.

A node is considered deepest if it has the maximum depth.
The subtree of a node includes the node itself and all its descendants.

---

Approach: Single-Pass DFS (Post-order)

For each node, return a pair:
    (candidate_node, depth)

Logic:
1. Recursively compute results for left and right subtrees.
2. If left depth > right depth:
      return left candidate with depth + 1
3. If right depth > left depth:
      return right candidate with depth + 1
4. If both depths are equal:
      current node is the LCA of all deepest nodes

This ensures the smallest subtree containing all deepest nodes.

---

Time Complexity:
- O(n), where n is number of nodes

Space Complexity:
- O(h), recursion stack (h = tree height)
"""


from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return (None, 0)

            left_node, lh = dfs(node.left)
            right_node, rh = dfs(node.right)

            if lh > rh:
                return (left_node, lh + 1)
            if rh > lh:
                return (right_node, rh + 1)

            # Equal depth: current node is LCA of deepest nodes
            return (node, lh + 1)

        return dfs(root)[0]


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    # Example:
    #        3
    #       / \
    #      5   1
    #     / \   \
    #    6   2   0
    #       / \
    #      7   4
    #
    # Deepest nodes: 7, 4, 0
    # Expected answer root value: 3

    root = TreeNode(
        3,
        TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
        TreeNode(1, None, TreeNode(0))
    )

    sol = Solution()
    ans = sol.subtreeWithAllDeepest(root)
    print(ans.
