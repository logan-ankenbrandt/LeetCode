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
        ans = []
        for i in range(len(nums)):
            for j in nums:
                if i + j == target:
                    # currently having difficulties accessing
                    # the index of the requested numbers
                    print(nums[i], nums[j])
        return ans