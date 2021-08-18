from typing import List
import collections
import snoop

@snoop
def runningSum(nums: List[int]) -> List[int]:
        """
        1. Goal
            - Given an array, create a new array with a running sum of the               values from the nums array.
        2. Examples
            - Example #1
                a. Input
                    i. nums = [1,2,3,4]
                b. Output
                    i. [1,3,6,10]
            - Example #2
                a. Input
                    i. nums = [1,1,1,1,1]
                b. Output
                    i. [1,2,3,4,5]
        3. Implementation
            - Summary
                a. While iterating over the array, store the sum of                 the values so far in the currSum variable while                     maintaining a dictionary with the key-value pairs                   being the index of the subarray and the sum of the                   values in the subarray. Append each currSum to the 
                res array.
            - Steps
                a. Initialize the dictionary using the                               collections.defaultdict(int) class with a lambda                     function that returns 0.
                b. Initialize the res variable to an empty list to                   store the values
                c. Initialize the currSum variable and set it to 
                0 to hold the sum of the running array.
                d. Loop through the index of the length of the
                array
                e. Add each element to the currSum variable on each                 pass
                f. Store the new element in the res array
        """
        res = []
        currSum = 0
        for i in range(0, len(nums)):
            currSum += nums[i]
            res.append(currSum)
        return res

print(runningSum([1,2,3,4]))