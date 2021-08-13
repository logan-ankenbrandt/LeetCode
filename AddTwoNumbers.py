# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        1. Goal
            - Steps
                a. List -> Int
                    i. Reverse the nodes of two linked lists
                        - Convert to a regular list?
                    ii. Join the values
                    iii. Convert them to an int
                d. Computation
                    i. Add the two integers together
                c. Int -> List
                    i. Convert to a string
                    ii. Split the values
                    iii. Reverse the values
                        - Convert to a linked list?
        2. Examples
            - Example #1
                a. Input
                    i. l1 = [2,4,3]
                    ii. l2 = [5,6,4]
                b. Output
                    i. [7,0,8]
                c. Explanation
                    i. Input
                        - l1 = [2,4,3] -> 342
                        - l2 = [5,6,4] -> 465
                        - 342 + 465
                    ii. Output
                        - 342 + 465 = 807
            - Example #2
                a. Input
                    i. l1 = [9,9,9,9,9,9,9]
                    ii. l2 = [9,9,9,9]
                b. Output
                    i. [8,9,9,9,0,0,0,1]
                c. Explanation
                    i. Input
                        - l1 = [9,9,9,9,9,9,9] -> 9999999
                        - l2 = [9,9,9,9] -> 9999
                        - 9999999 + 9999
                    ii. Output
                        - 9999999 + 9999 = 89990001
                
        """