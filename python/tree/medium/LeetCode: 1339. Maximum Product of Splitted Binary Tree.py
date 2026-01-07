"""
LeetCode: 1339. Maximum Product of Splitted Binary Tree (Medium)
Problem link: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
Author: Aditya Pandey
Date: 2025-12-30

Problem:
Given the root of a binary tree, split the tree into two subtrees by removing
one edge such that the product of the sums of the two resulting subtrees
is maximized.

Return the maximum product modulo 10^9 + 7.

---

Approach: Tree DFS + Subtree Sum

Key idea:
- If we cut an edge, the tree splits into:
    - a subtree with sum = sub
    - the remaining tree with sum = total - sub
- The product becomes: sub × (total - sub)
- We need to maximize this value.

Steps:
1. Perform a DFS to compute the total sum of the tree.
2. Perform another DFS to compute subtree sums.
3. For each subtree, consider it as one part of the split.
4. Track the maximum product seen.

---

Why DFS?
- Subtree sums can be computed naturally using post-order traversal.
- Ensures each possible split is considered exactly once.

---

Time Complexity:
- O(n), where n is the number of nodes

Space Complexity:
- O(n) due to recursion stack
"""


from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        # First DFS to compute total sum of the tree
        def totalSum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)
        self.max_product = 0

        # Second DFS to compute subtree sums and maximize product
        def subtreeSum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = subtreeSum(node.left)
            right = subtreeSum(node.right)
            sub = node.val + left + right

            # Consider splitting here
            self.max_product = max(self.max_product, sub * (total - sub))
            return sub

        subtreeSum(root)
        return self.max_product % MOD


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    # Example:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    #
    # Expected: 110

    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, None, TreeNode(6))
    )

    sol = Solution()
    print(sol.maxProduct(root))  # Expected: 110
