"""
LeetCode: 2049. Count Nodes With the Highest Score (Medium)
Problem link: https://leetcode.com/problems/count-nodes-with-the-highest-score/
Author: Aditya Pandey
Date: 2026-01-15

Problem:
You are given a tree rooted at node 0 represented by a `parents` array,
where parents[i] is the parent of node i.

The **score** of a node is defined as:
- The product of the sizes of all connected components formed
  when the node is removed from the tree.

Return the number of nodes that achieve the **highest score**.

---

Approach: Tree DFS + Subtree Size Calculation

Key idea:
- Removing a node splits the tree into multiple components:
  1. Each child subtree
  2. The remaining part of the tree (parent side)

For each node:
1. Compute the size of each child subtree using DFS.
2. Multiply all child subtree sizes to the score.
3. Multiply by the remaining nodes (n - subtree_size - 1), if > 0.
4. Track the maximum score and count how many nodes achieve it.

---

Why DFS?
- Subtree sizes are naturally computed using post-order traversal.
- Each node is processed once.

---

Time Complexity:
- O(n), where n is the number of nodes

Space Complexity:
- O(n), for adjacency list and recursion stack
"""


from typing import List
from collections import defaultdict


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        adj = defaultdict(list)

        # Build tree
        for child in range(n):
            parent = parents[child]
            if parent != -1:
                adj[parent].append(child)

        max_score = 0
        count = 0

        def dfs(node: int) -> int:
            nonlocal max_score, count
            score = 1
            size = 0  # size of current subtree excluding parent side

            for child in adj[node]:
                child_size = dfs(child)
                size += child_size
                score *= child_size

            # Remaining part of tree after removing this node
            remaining = n - size - 1
            if remaining > 0:
                score *= remaining

            # Update global maximum score
            if score == max_score:
                count += 1
            elif score > max_score:
                max_score = score
                count = 1

            return size + 1

        dfs(0)
        return count


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.countHighestScoreNodes([-1, 2, 0, 2, 0]))
    # Expected: 3

    print(sol.countHighestScoreNodes([-1, 2, 0]))
    # Expected: 2
