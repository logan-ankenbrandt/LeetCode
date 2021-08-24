from typing import List


class SparseVector:
    """
    1. Goal
        - Compute the product between the indexes of numbers in 
        two arrays and return the sum of all the products
    2. Example
        - Example #1
            a. Input
                i. nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
            b. Output
                i. 8
            c. Explanation
                i. v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
                v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
    3. Implementation
        - Summary
            a. In the class, one list is initialized and held in self and
            the indexes are multiplied and summed by the indexes of the list 
            stored in the vec parameter in the dotProduct() function.
        - Steps
            a. Initialize a list in the constructor
                i. This will be created by calling the SparseVector()
                class and storing a list as the parameter
            b. Pass that list as self in the dotProduct() function along with
            vec
                i. Vec is set to the SparseVector() class - this indicates
                that the dotProduct() function will only be ran when there
                is another list stored in a class initialization.
            c. In the dotProduct() function, 
                i. Initialize a list
                ii. Loop through both lists using
                    - Self.nums to reference the list in the current class
                    - Vec.nums to reference the list stored in the second class
                    initialization
                    - The zip() operator to create tuples where each element in 
                    both arrays are stored together by index
                iii. Within the loop, append the product of each tuple in the
                array
                iv. Return the sum() of the array
    """

    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors

    def dotProduct(self, vec: 'SparseVector') -> int:
        l = []
        for i, j in zip(self.nums, vec.nums):
            l.append(i * j)
        return sum(l)
