"""
LeetCode: 2641. Cousins in Binary Tree II (Medium)
Problem link: https://leetcode.com/problems/cousins-in-binary-tree-ii/
Author: Aditya Pandey
Date: 2026-01-14

Problem:
Given the root of a binary tree, replace the value of each node with the sum
of its cousins' values.

Two nodes are cousins if:
- They are on the same level
- They do NOT share the same parent

The root node has no cousins, so its value should be replaced with 0.

---

Approach: Level Order Traversal (BFS)

Key idea:
- Traverse the tree level by level using BFS.
- For each level:
  1. Compute the total sum of all child nodes at the next level.
  2. For each child, subtract the sum of its siblings' original values.
  3. Assign: new_value = level_sum - sibling_sum

Steps:
1. Initialize BFS queue with the root.
2. Set root value to 0.
3. For each level:
   - Track total sum of next-level nodes.
   - Track sibling sums for each child.
4. Update values of children before moving to the next level.

---

Why this works:
- Cousins = all nodes at same level EXCEPT siblings.
- Level sum − sibling sum gives exactly the cousin sum.

---

Time Complexity:
- O(n), where n is the number of nodes

Space Complexity:
- O(n), for the BFS queue
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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        q = deque([root])
        root.val = 0

        while q:
            level_sum = 0
            next_level = []

            for _ in range(len(q)):
                node = q.popleft()
                sibling_sum = 0

                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val

                if node.left:
                    level_sum += node.left.val
                    next_level.append((node.left, sibling_sum))
                if node.right:
                    level_sum += node.right.val
                    next_level.append((node.right, sibling_sum))

            # Update values for next level nodes
            for child, sib_sum in next_level:
                child.val = level_sum - sib_sum

            q.extend([child for child, _ in next_level])

        return root


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    # Example:
    #        5
    #       / \
    #      4   9
    #     / \   \
    #    1  10   7
    #
    # Expected tree values:
    #        0
    #       / \
    #      0   0
    #     / \   \
    #    7   7   11

    root = TreeNode(
        5,
        TreeNode(4, TreeNode(1), TreeNode(10)),
        TreeNode(9, None, TreeNode(7))
    )

    sol = Solution()
    sol.replaceValueInTree(root)

    print(root.val, root.left.val, root.right.val)  # 0 0 0
