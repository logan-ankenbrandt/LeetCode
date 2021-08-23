from collections import OrderedDict
class LRUCache(OrderedDict):
    """
    1. Goal
        a. Write a series of functions within the LRUCache class that
        has the ability to return the key, in the get() function, and update
        the value of the key, within the put() function. 
    2. Examples
        a. Example #1
            i. Input
                - ["LRUCache", "put", "put", "get", "put", "get", "put", 
                "get", "get", "get"]
                - [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], 
                [1], [3], [4]]
                - Explanation
                    a. At index 0, the LRUCache is initialized and set to 2
                    b. At index 1, the put() function is called and the key value
                    pair 1, 1 is inserted
                    c. At index 3, the get() function is called on the 1 key and
                    it's value is returned.
            ii. Output
                - [null, null, null, 1, null, -1, null, -1, 3, 4]
            iii. Explanation
                - Since indexes 0-2 are simply the initialization of the dictionary
                and the values inside of it, the values returned are null.
                - In index 3, 1 is called in the get() function, and it's value is
                returned
                - In index 5, -1 is returned since it is booted out by the last
                put() call, and 3: 3 is inserted in it's place.
    3. Implementation
        a. Summary
            i. In the __init__() constructor, set the dictionary's max length (of 
            keys), to the capacity integer, and use the get() and put() functions
            to return or insert values within the dictionary.
        b. Steps
            - Use the constructor to initialize the max length of key-pair values.
            - In the get() function, write
                a. A conditional statement that returns -1 if the key
                is not in the dictionary
                b. A statement that moves the key to the end of the dictionary
                when it is called
                    i. This ensures that, since this an OrderedDict, the correct
                    element is deleted when the capacity is exceeded
                c. A return statement that returns the key from the dictionary
            - In the put() function, write
                a. A conditional statement that checks if the key
                is in the dictionary and moves it to the end of the
                dictionary if it is
                    i. This ensures that, since this an OrderedDict, the correct
                    element is deleted when the capacity is exceeded
                b. A statement that sets the key to the value that is
                set as a parameter in the put() function
                c. A conditional statement that 
                    i. Checks if the length of the dictionary is greater than the 
                    capacity set in the constructor
                    ii. If so, set popitem() to last = false
                        - This will remove the first item in the dictionary
        c. Issues
            - Issue #1
                a. Description
                    i. Did not know to use OrderedDict() as a means to preserve
                    the order that items are inserted into the dictionary
                b. Resolution
                    i. Learned that when I need to track the order of entry for
                    a dictionary, use OrderedDict
            - Issue #2
                a. Description
                    i. Did not realize that by setting OrderedDict()
                b. Resolution


    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


lRUCache = LRUCache(2)
print(lRUCache.put(1, 1))
print(lRUCache.get(1))