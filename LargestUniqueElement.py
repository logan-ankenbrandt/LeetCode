from typing import List
from collections import Counter
import snoop as dog

@dog
def largestUniqueNumber(nums: List[int]) -> int:
    """
    1. Goal
        - Find the largest unique number in a list of numbers
    2. Examples
        - Example #1
            a. Input
                i. nums = [5,7,3,9,4,9,8,3,1]
            b. Output
                i. 8
        - Example #2
            a. Input
                i. nums = [5,7,3,9,4,9,8,3,1,6,8]
            b. Output
                i. 7
    3. Implementation
        - Summary
            a. Create a Counter object and an empty list, loop through
            the dictionary and append the unique numbers to the list,
            write a conditional to return the largest number in the list
            if it is not empty
        - Steps
            a. Create a Counter object and an empty list
            b. Loop through the dictionary and append the unique numbers
            to the list
            c. Write a conditional to return the largest number 
            in the list if it is not empty
    """
    n = Counter(nums)
    l = []
    for key, values in n.items():
        if values == 1:
            l.append(key)
    
    if len(l) > 0:
        return max(l)
    else:
        return -1

print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))