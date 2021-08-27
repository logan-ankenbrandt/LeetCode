def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    """
    1. Goal
        - Return the sum of the numbers in a BT that are within the ranges
        low and high
    2. Examples
        - Example #1
            a. Input
                i. root = [10,5,15,3,7,null,18], low = 7, high = 15
            b. Output
                i. 32
    3. Implementation
        - Steps
            a. Initialize the ans variable for incrementation
            and set it to 0
            b. Initialize the t variable and set it to the root of the BST
            wrapped in a list
            c. Write a while loop over t that performs the following tasks while
            t exists:
                i. Stores the current node of the BST in the node variable and
                removes it from the tree with pop()
                ii. Performs a conditional that checks if node:
                    - Is greater than or equal than low or less than or equal to high
                        a. This would mean it falls between the range & it's value should be
                        incremented to the answer
                    - Is greater than the node
                        b. This would mean we've traveled too far within the tree & need to
                        go to the next node on the left to check if that node falls between the


        - Summary
    """
    ans = 0
    t = [root]
    while t:
        node = t.pop()
        if node:
            if low <= node.val <= high:
                ans += node.val
            if low < node.val:
                t.append(node.left)
            if node.val < high:
                t.append(node.right)

    return ans
