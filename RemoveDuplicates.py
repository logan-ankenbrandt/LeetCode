from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
        """
        1. Goal
            - Remove the duplicates from a sorted array
        2. Examples
            - Example #1
                a. Input
                    i.nums = [1,1,2] 
                b. Output
                    i. 2, nums = [1,2,_]
            - Example #2
                a. Input
                    i. nums = [0,0,1,1,1,2,2,3,3,4]
                b. Output
                    i. 5, nums = [0,1,2,3,4,_,_,_,_,_]
        3. Implementation
            - Flow
            - Steps
                a. Create a sorted set of the nums array to remove the duplicats
                b. Return the set
        """
        nums = sorted(set(nums))
        return nums

print(removeDuplicates(None,[1,1,2]))