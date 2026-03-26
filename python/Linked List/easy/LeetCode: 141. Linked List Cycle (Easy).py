"""
LeetCode: 141. Linked List Cycle (Easy)
Problem Link: https://leetcode.com/problems/linked-list-cycle/
Author: Aditya Pandey
Date: 2026-03-26

------------------------------------------------------------
Problem:
Given the head of a linked list, return True if there is a cycle in the linked list.
Otherwise, return False.

A cycle exists if some node can be reached again by continuously following next pointers.

------------------------------------------------------------
Pattern:
Two Pointers / Fast and Slow Pointer

------------------------------------------------------------
Approach:
Use two pointers:
- slow moves 1 step at a time
- fast moves 2 steps at a time

If the linked list has a cycle:
- fast will eventually catch slow inside the cycle

If the linked list has no cycle:
- fast will reach None

------------------------------------------------------------
Why This Works:
- In a cycle, the fast pointer keeps gaining on the slow pointer
- Since fast moves faster, they must meet if a cycle exists
- If there is no cycle, fast pointer reaches the end first

------------------------------------------------------------
Time Complexity:
O(n)

Space Complexity:
O(1)

------------------------------------------------------------
Things to Pay Attention To:
- Check both `fast` and `fast.next` before moving fast
- Compare pointers using `is` / `==` based on node identity
- Do not use extra space unless needed
------------------------------------------------------------
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
