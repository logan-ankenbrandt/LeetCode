from typing import List
from collections import Counter
import snoop

@snoop
def repeatedNTimes(nums: List[int]) -> int:
        """
        1. Goal
            - Return the repeated number in an array
        2. Examples
            - Example #1
                a. Input
                    i. nums = [1,2,3,3]
                b. Output
                    i. 3
            - Example #2
                a. Input
                    i. nums = [2,1,2,5,3,2]
                b. Output
                    i. 2
        3. Implementation
            - Summary
                a. Initialize a Counter() variable to count the number of instances of the elements
                in the array, loop through the dictionary, return the key if the value is greater
                than one
            - Steps
                a. Initialize a counted dictionary with the Counter() class
                b. Loop throuhg the items in the dictionary
                c. Check if the values in the dictionary are greater than one
                d. Return the key that is greater than one
        """
        
        n = Counter(nums)
        for key, value in n.items():
            if value > 1:
                return key

print(repeatedNTimes([1,2,3,3]))