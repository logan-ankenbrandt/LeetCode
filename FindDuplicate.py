from typing import List
from collections import Counter


def findDuplicates(self, nums: List[int]) -> List[int]:
    """
    1. Goal
        - Find duplicates in an array and return them as a list
    2. Examples
        - Example #1
            a. Input
                i. [4,3,2,7,8,2,3,1]
            b. Output
                i. [2,3]
    3. Implementation
        - Steps
            a. Initialize an empty list
            b. Iterate through the key value pairs in a Counter() instance
            of the list
            c. Write a conditional that checks if the value is greater than
            1 and appends it to the new list
            d. Return the new list
        - Summary
            a. Used a Counter() instance to count the number of times each
            number appears in the list and appended the number to a list if
            the count was greater than 1
    """
    
    l = []
    for key, value in Counter(nums).items():
        if value > 1:
            l.append(key)
    return l
