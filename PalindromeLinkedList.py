from typing import Optional
import snoop

@snoop
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

@snoop
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        1. Goal
            - Check if a linked list is a palindrome
        2. Examples
            - Example #1
                a. Input
                    i. 1 -> 2 -> 3 -> 2 -> 1 
                b. Output
                    i. True
        3. Implementation
            - Steps
                a. Initialize an empty list
                b. Write a while loop to go through the linked list and
                append the values to the empty list
                c. Reverse the list
                d. Compare the reversed list to the original list and return true
                if they are the same
            - Summary
                a. This solution simply goes through the linked list and appends
                the values to a list. Then it reverses the list and compares the
                reversed list to the original list.
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        rev = nums[::-1]
        if nums == rev:
            return True
        else:
            return False

