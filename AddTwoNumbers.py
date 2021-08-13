
class ListNode(object):
    def __init__(self, x):
        """
        This is the function to initialize
        a node for a singly linked list.
        """
        self.val = x
        self.next = None


def find_length(head):
    """
    This is the function to find the length
    of a linked list.
    """
    curr = head
    count = 0
    while curr is not None:
        count += 1
        curr = curr.next
    return count

def convertList(head):
    """
    This is the function to convert the
    linked list to a number.
    """
    len = find_length(head)
    arr = []
    curr = head
    while curr is not None:
        arr.append(curr.val)
        curr = curr.next
   
    return arr, len

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
        3. Params:
            - l1: Linked List
            - l2: Linked List
        4. Implementation
        """
        list_1 = convertList(l1)
        list_2 = convertList(l2)
        print(list_1, list_2)

print(convertList(self=None, l1=[2, 3, 4], l2=[5, 6, 4]))

"""
1. Issues
    - Currently receiving these errors:
        a. print(addTwoNumbers(None, [2, 3, 4], [5, 6, 4]))
        b. list_1 = convertList(l1)
        c. len = find_length(head)
        d. curr = curr.next
        e. AttributeError: 'list' object has no attribute 'next'
    - I believe the issue is that the lists that are being passed through,

"""