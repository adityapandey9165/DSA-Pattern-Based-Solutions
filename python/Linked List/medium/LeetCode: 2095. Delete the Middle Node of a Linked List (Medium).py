"""
LeetCode: 2095. Delete the Middle Node of a Linked List (Medium)
Problem Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
Author: Aditya Pandey
Date: 2026-06-14

------------------------------------------------------------
Problem:
Given the head of a linked list, delete the middle node and return
the head of the modified list.

If the list has only one node, return None.

For an even-length list, delete the second middle node.

------------------------------------------------------------
Pattern:
Fast and Slow Pointer

------------------------------------------------------------
Approach:
We use two pointers:
- slow moves 1 step at a time
- fast moves 2 steps at a time

We also keep a `prev` pointer to track the node before `slow`.

Steps:
1. Handle edge case:
   - If list has 0 or 1 node, return None
2. Move slow and fast together until fast reaches the end
3. At the end:
   - slow points to the middle node
   - prev points to the node before middle
4. Delete the middle node by:
       prev.next = slow.next

------------------------------------------------------------
Why this works:
Fast pointer moves twice as fast as slow.
So when fast reaches the end:
- slow is at the middle
- prev is just before the middle

This lets us remove the middle node in one pass.

------------------------------------------------------------
Time Complexity:
O(n)

We traverse the list once.

------------------------------------------------------------
Space Complexity:
O(1)

We use only a few pointers.

------------------------------------------------------------
Things to Pay Attention To:
- If the list has only one node, return None
- Keep track of `prev` before moving `slow`
- For even length, delete the second middle node
- Do not use extra arrays or stacks

------------------------------------------------------------
Common Mistakes:
- Forgetting the single-node edge case
- Not updating `prev` before moving `slow`
- Deleting the wrong middle node in even-length lists
- Using extra space when it is not needed
------------------------------------------------------------
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: 0 or 1 node
        if not head or not head.next:
            return None

        prev = None
        slow = head
        fast = head

        # Find middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Remove middle node
        if prev:
            prev.next = slow.next

        return head


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def build_list(values):
        dummy = ListNode(0)
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def to_list(head):
        out = []
        while head:
            out.append(head.val)
            head = head.next
        return out

    sol = Solution()

    head = build_list([1, 3, 4, 7, 1, 2, 6])
    print(to_list(sol.deleteMiddle(head)))   # Expected: [1, 3, 4, 1, 2, 6]

    head = build_list([1, 2, 3, 4])
    print(to_list(sol.deleteMiddle(head)))   # Expected: [1, 2, 4]

    head = build_list([2, 1])
    print(to_list(sol.deleteMiddle(head)))   # Expected: [2]

    head = build_list([1])
    print(sol.deleteMiddle(head))            # Expected: None
