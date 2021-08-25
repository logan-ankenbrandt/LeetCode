class MyQueue:
    """
    1. Goal
        - Implement a FIFO
    2. Examples
        - Example #1
            a. Input
                i. ["MyQueue", "push", "push", "peek", "pop", "empty"]
                    [[], [1], [2], [], [], []]
            b. Output
                i. [null, null, null, 1, 1, false]
            c. Explanation
                i. "MyQueue" -> myQueue = new MyQueue() -> Initializes an instance of the class
                ii. "push" -> myQueue.push(1) -> [1] -> Adds 1 to the queue
                iii. "push" -> myQueue.push(2) -> [1, 2] -> Adds 2 to the queue
                iv. "peek" -> myQueue.peek() -> 1 -> Returns the value from the front of the queue
                v. "pop" -> myQueue.pop() -> 1, [2] -> Removes the value from the front of the queue
                and returns it
                vi. "empty" -> myQueue.empty() -> false, [2] -> Checks if the array is empty and returns a boolean
    1. Implementation
        - Issues
        - Steps
            a. Initialize the data variable in the constructor & set it to
            an empty list
            b. Write the push(x) method that takes in an integer x and adds it to
            the queue
            c. Write the pop() method that removes the element at the front of the
            queue and returns it
            d. Write the peek() method that returns the element at the front of the
            queue without removing it
            e. Write the empty() method that checks if the queue is empty and
            returns a boolean
        - Summary
            a. Simply utilized OOP and the queue data structure to implement the
            FIFO
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.data.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.data[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.data) == 0:
            return True
        else:
            return False
