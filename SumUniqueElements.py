from typing import List
import snoop

@snoop
def sumOfUnique(nums: List[int]) -> int:
        """
        1. Goal
            - Return the sum of all unique elements
        2. Examples
            - Example #1
                a. Input
                    i. nums = [1, 2, 3, 2]
                b. Output
                    i. 4
            - Example #2
                a. Input
                    i. nums = [1, 1, 1, 1, 1]
                b. Output
                    i. 0
         3. Implementation
            - Summary
                a. Count each element, add the elements that
                are unique to a count
            - Steps
                a. Initailize a count variable to 0
                b. Iterate through the list
                c. If the count of the current element
                in the list equals 1, add the element
                to the count variable 
        """
        c = 0
        for i in nums:
            if nums.count(i) == 1:
                c += i
        return c

print(sumOfUnique([1, 1, 1, 1, 1]))