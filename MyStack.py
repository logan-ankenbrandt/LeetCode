class MyStack:

    """
    1. Goal 
        - Implement a LIFO using only two queues
    2. Examples
        - Example #1
            a. Input
                i. ["MyStack", "push", "push", "top", "pop", "empty"]
                    [[], [1], [2], [], [], []]
            b. Output
                i. [null, null, null, 2, 2, false]
            c. Explanation
                i. "MyStack" -> myStack = new Mystack() -> Initializes the class instance
                ii. "push" -> myStack.push(1) -> Adds 1 to the stack
                iii. "push" -> myStack.push(2) -> Adds 2 to the stack
                iv. "top" -> myStack.top() -> 2 -> 
                Returns the element at the top (or back) of the stack
                v. "pop" -> myStack.pop() -> 2 -> 
                Deletes the element at the top (or back) of the stack and returns it
                vi. "empty" -> myStack.empty() -> False -> Checks if there are elements in the stack & returns a boolean   
    3. Implementation
        - Issues
            a. What data structure, dictionary or list, should I use to initialize the commands
            and input?
        - Steps
            a. Initialize the data variable in the constructor & set it to
            an empty list
            b. Write the push(x) method that takes in an integer x and adds it to 
            the stack
            c. Write the pop() method that removes the element at the top of the
            stack and returns it
            d. Write the top() method that returns the element at the top of the
            stack without removing it
            e. Write the empty() method that checks if the stack is empty and
            returns a boolean
        - Summary
            a. Simply utilized OOP and the queue data structure to implement the
            LIFO
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return (self.data.pop())

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.data[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.data) == 0:
            return True
        else:
            return False
