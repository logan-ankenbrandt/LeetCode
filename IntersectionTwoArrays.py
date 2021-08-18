from typing import List
import snoop

@snoop
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        1. Goal
            - Return the elements that are present across multiple arrays
        2. Examples
            - Example #1
                a. Input
                    i. nums1 = [1,2,2,1], nums2 = [2,2]
                b. Output
                    i. [2]
            - Example #1
                a. Input
                    i. nums1 = [4,9,5], nums2 = [9,4,9,8,4]
                b. Output
                    i. [9, 4]
        3. Implementation
            - Summary
                a. Initialize empty list, loop over list 1 
                and write a conditional to check if the element is 
                in list 2, if it is, append it to the list,
                return a set of the list to remove duplicates
            - Steps
                a. Initialize empty list
                b. Loop over list 1
                c. Write a conditional to check if the element is
                in list 2
                d. If it is, append it to the list
                e. Return a set of the list to remove duplicates
            - Issues
                a. I did not realize that you could 
                check if an element was in a list using the "in" keyword
                for a coniditional
        """
        l = []
        for i in nums1:
            if i in nums2:
                l.append(i)
        return set(l)