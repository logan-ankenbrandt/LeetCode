from typing import List
import snoop

@snoop
def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
        """
        1. Goal
            - At each number, return the amount of numbers
            in the array that are smaller than the current
            number.
        2. Examples
            - Example #1
                a. Input
                    i. nums = [8,1,2,2,3]
                b. Output
                    i. [4,0,1,1,3]
            - Example #2
                a. Input
                    i. [6,5,4,8]
                b. Output
                    i. [2,1,0,3]
        3. Implementation
            - Summary
                a. 
            - Steps
        """
        i, count = 0, 0
        arr = []
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
            arr.append(count)
        return arr

print(smallerNumbersThanCurrent([8,1,2,2,3]))