from typing import List


def removeElement(nums: List[int], val: int) -> int:
    """
    1. Goal
        - Remove all occurences of an element in an array
        and print the new length of the array.
    2. Examples
        - Exampe #1
            a. Input
                i. [3,2,2,3]
            b. Output
                i. 2
    3. Implementaiton
        - Use a while loop to remove the element of interest
        while it is still in the array.
    """   
    while val in nums:
        nums.remove(val)
    return len(nums)

print(removeElement([3, 2, 2, 3], 3))