from typing import List


def searchInsert(self, nums: List[int], target: int) -> int:
    """
    1. Goal
        - Return the index of a target in a sorted array and
        where the index would be if it is not in an array.
    2. Examples
        - Example #1
            a. Input
                i. nums = [1,3,5,6], target = 5
            b. Output
                i. 2
    3. Implementation
        - Steps
            a. Write a conditional that
                i. Checks if the target is in the list
                ii. Returns the index of the target using the .index()
                function.
                iii. Otherwise, it appends the target to the list
                iv. Sorts the list
                v. Returns the index of the newly inserted target
        - Summary
            a. Use a conditional to check if a target is in an array and
            return the index - otherwise, insert the target & sort the array to return
            the correct index.
    """

    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)
