from typing import List
import snoop

@snoop
def numIdenticalPairs(nums: List[int]) -> int:
        """
        1. Goal
            - Return the amount of pairs that are identical
        2. Examples
            - Example #1
                a. Input
                    i. nums = [1,2,3,1,1,3]
                b. Output
                    i. 4
                c. Explanation
                    i. There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
            - Example #2
                a. Input
                    i. nums = [1,1,1,1]
                b. Output
                    i. 6
                c. Explanation
                    i. (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)
        3. Implementation
            - Summary
                a. Loop over the array, check if the current element is equal to the next element, and add to the
                count if it is
            - Steps
                a. Initialize an i variable and set it to 0 to avoid nested loops
                    i. This creates an index to compare j against
                a. Initialze a count variable for the amount of pairs and a sorted array 
                to save time
                b. Loop over the range of the length of the array and set the inital index of j to i + 1
                c. Write an conditional statement with the following:
                    i. If the element at i is equal to the element at j, add one to the count
                    ii. Otherwise, continue
                d. Return the count
        """
        i, ans, nums = 0, 0, sorted(nums)
        for j in range(1, len(nums)):
            print(nums[i], nums[j])
            if nums[i] == nums[j]: 
                ans += (j - i)
            else: 
                i = j
        return ans

print(numIdenticalPairs([1,2,3,1,1,3]))