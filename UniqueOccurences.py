from collections import Counter
from typing import List

def uniqueOccurrences(self, arr: List[int]) -> bool:
    """
    1. Goal
        - Return True if all values of the array are
        unique, else return False.
    2. Examples
        - Example #1
            a. Input
                i. arr = [1,2,2,1,1,3]
            b. Output
                i. True
        - Example #2
            a. Input
                i. arr = [1,2]
            b. Output
                i. False
    3. Implementation
        - Steps
            a. Initialize a Counter object to
            count the number of times each element 
            a appears in the array.
            b. Initialize an empty array.
            c. Iterate through the dictionary and append
            the values to the list
            d. Initialize a new Counter object to
            count the number of times each value is in
            the values list.
            e. Write a conditional to check if the
            length of the values of the dictionary is
            not equal to the length of the list & return
            True or False depending on the boolean.
        - Summary
            a. Use Counter twice to check the amount of appearances
            of an element in the array.
    """
    
    c = Counter(arr)
    l = []
    for value in c.values():
        l.append(value)

    n = Counter(l)
    if len(n) != len(l):
        return False
    else:
        return True
