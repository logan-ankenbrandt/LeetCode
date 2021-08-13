from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1.Goal
            - Take a list of integers, nums, and return the index of the two numbers
            in the list that return the target.
        2. Examples
            - Example #1
                a. Input
                    i. nums = [2, 7, 11, 15]
                    ii. target = 9
                b. Output
                    i. [0, 1]
            - Example #2
                a. Input
                    i. nums = [3, 8, 15, 12]
                    ii. target = 27
                b. Output
                    i. [2, 3]
        3. Implementation
            - Brute Force
                a. Iterate through the array, adding each element to the other, and keep
                track of the indexes of the numbers
        """
        for i in range(len(nums)):
            # In this for loop, len is used to count the elements in the list,
            # and the range is used to create an index of the list to iterate through
            for j in range(i + 1, len(nums)):
                # In this for loop, len is used to count the elements in the list,
                # i + 1 is used to indicate which index the newly initialized variable
                # j will be assigned, and range is used to define the index
                if nums[i] + nums[j] == target:
                    # In this if statement, nums[i] + nums[j] is used to add the two
                    # numbers together, and target is used to compare the sum to the
                    # target number
                    return [i, j]

print(twoSum(None, [2, 7, 11, 15], 9))