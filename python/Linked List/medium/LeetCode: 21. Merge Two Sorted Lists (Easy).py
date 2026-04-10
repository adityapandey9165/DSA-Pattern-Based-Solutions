"""
LeetCode: 21. Merge Two Sorted Lists (Easy)
Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
Author: Aditya Pandey
Date: 2026-04-06

------------------------------------------------------------
Problem:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the merged list.

------------------------------------------------------------
Pattern:
Linked List Traversal + Dummy Node

------------------------------------------------------------
Approach:
We use two pointers, one for each linked list.

At every step:
1. Compare the current nodes of list1 and list2
2. Attach the smaller node to the merged list
3. Move the pointer of the list from which the node was taken
4. Continue until one list becomes empty
5. Attach the remaining part of the other list

A dummy node is used so we do not need special handling for the head.

------------------------------------------------------------
Why this works:
Both lists are already sorted.
So at each step, choosing the smaller current node keeps the merged list sorted.

------------------------------------------------------------
Time Complexity:
O(m + n)

Space Complexity:
O(1)
(ignoring the output list nodes)

------------------------------------------------------------
Things to Pay Attention To:
- Use a dummy node to simplify list construction
- Do not create unnecessary new nodes
- Attach the remaining part directly after one list ends
- This is an iterative merge, not sorting from scratch

------------------------------------------------------------
Common Mistakes:
- Forgetting to connect the leftover nodes
- Not using a dummy node and making head handling messy
- Rebuilding all nodes unnecessarily
------------------------------------------------------------
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next

        # attach remaining nodes
        p.next = list1 if list1 else list2

        return dummy.next
