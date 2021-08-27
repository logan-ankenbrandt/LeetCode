from typing import List
import math


def productExceptSelf(self, nums: List[int]) -> List[int]:
    """
    1. Goal
        - Given an array of integers, find out the product of all the elements
        except the current element.
    2. Examples
        - Example #1
            a. Input
                i. nums = [1, 2, 3, 4]
            b. Output
                i. [24, 12, 8, 6]
    3. Implementation
        - Steps
            a. Initialize a product variable and set it to
            the product of all the elements in the array.
            b. Initialize a result variable and set it to an empty list.
            c. Loop through the array and and write a conditional that
                i. Checks if the current variable is equal to 0
                ii. If it isn't, then 
                    - Append the product variable divided by the current 
                    variable
                iii. If it is, then
                    - Set a variable to the index of the 0
                    - Delete the number at that index
                    - Append the product of the entire array to the result
                    - Re-insert the number at it's correct index
            d. Return the result
        - Summary
            a. Used the prod() function from the math library to divide the
            variables agains the product of the array and stored it into a
            resultant array - if it equalled 0 I deleted the number from the
            array, performed the prod() function and stored it into the result, 
            and re-inserted the number at it's correct index.
    """
    prod = math.prod(nums)
    f = []
    for i in nums:
        if i > 0 or i < 0:
            f.append(int(prod / i))
        else:
            index = nums.index(i)
            del nums[index]
            f.append(math.prod(nums))
            nums.insert(index, i)
    return f
