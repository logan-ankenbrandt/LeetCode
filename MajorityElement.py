from collections import Counter
from typing import List

def majorityElement(self, nums: List[int]) -> int:
    """
    1. Goal
        a. Return the most frequent value in a list
    2. Examples
        a. Example #1
            - Input
                i. nums = [3, 2, 3]
            - Output
                i. 3
    3. Implementation
        a. Summary
            - Use counter to count the frequency, find the max
            of the values in the dict, loop through the dict,
            if a value equals the max value, return the key
        b. Steps
            - Count the frequency of the numbers in the list
            w the Counter() module and set it to a variable
            - Set the max of the values to a variable
            - Loop through the items in the dictionary
            - Write a conditional to check if the values in the dict
            are equal to the max
            - If it does, return the key
    """
    
    c = Counter(nums)
    m = max(c.values())
    for key, values in c.items():
        if values == m:
            return key
