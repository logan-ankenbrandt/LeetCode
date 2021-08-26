from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Goal
            a. Reverse a linked list
        2. Examples
        3. Implementation
            a. Set the current variable to the head of the
            linked list
            b. Set the previous variable to None
            c. While the current variable is not None:
                i. Set the next variable to the current variable
                ii. Set the current variable to the previous variable
                iii. Set the previous variable to the current variable
            d. Return the previous variable
        """
        
        cur = head
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
