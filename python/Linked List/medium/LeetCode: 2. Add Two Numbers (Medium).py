"""
LeetCode: 2. Add Two Numbers (Medium)
Problem Link: https://leetcode.com/problems/add-two-numbers/
Author: Aditya Pandey
Date: 2026-03-26

------------------------------------------------------------
Problem:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

Example:
l1 = 2 -> 4 -> 3
l2 = 5 -> 6 -> 4
Output = 7 -> 0 -> 8

------------------------------------------------------------
Pattern:
Linked List Traversal + Carry Handling

------------------------------------------------------------
Approach:
Use two pointers to traverse both lists node by node.

At each step:
1. Read current digit from l1 if available, otherwise 0
2. Read current digit from l2 if available, otherwise 0
3. Add both digits with carry
4. Create a new node for current digit = sum % 10
5. Update carry = sum // 10

We use a dummy node to simplify list construction.

------------------------------------------------------------
Why This Works:
- Digits are stored in reverse order, so addition can be done from head to tail
- Carry is propagated exactly like normal addition
- Dummy node avoids special handling for the head

------------------------------------------------------------
Time Complexity:
O(max(m, n))

Space Complexity:
O(max(m, n))
(for the output list)

------------------------------------------------------------
Things to Pay Attention To:
- Do not forget the final carry
- Use 0 when one list becomes shorter than the other
- Dummy node simplifies result handling
- This is reverse-order addition, not forward-order
------------------------------------------------------------
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        cur = dummy

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            cur.next = ListNode(total % 10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# ------------------------------------------------------------
# Helper methods for interview / local testing
# ------------------------------------------------------------
def build_linked_list(values):
    """
    Build a linked list from a Python list.

    Example:
        [2, 4, 3] -> 2 -> 4 -> 3
    """
    dummy = ListNode(0)
    cur = dummy
    for val in values:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head):
    """
    Convert linked list back to Python list.
    Useful for debugging / verifying output.
    """
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# -----------------------
# Quick tests for local verification
# -----------------------
if __name__ == "__main__":
    sol = Solution()

    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])

    ans = sol.addTwoNumbers(l1, l2)
    print(linked_list_to_list(ans))   # Expected: [7, 0, 8]

    l1 = build_linked_list([0])
    l2 = build_linked_list([0])

    ans = sol.addTwoNumbers(l1, l2)
    print(linked_list_to_list(ans))   # Expected: [0]

    l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = build_linked_list([9, 9, 9, 9])
    ans = sol.addTwoNumbers(l1, l2)
    print(linked_list_to_list(ans))   # Expected: [8, 9, 9, 9, 0, 0, 0, 1]
