from typing import List
import collections
import snoop

@snoop
def subarrayk(nums: List[int], k: int) -> int:
        """
        1. Goal 
            - List the amount of subarrays that, when added together, are equivalent to k
        2. Examples
            - Example #1
                a. Input
                    i. nums = [1,1,1], k = 2
                b. Output
                    i. 2           
            - Example #1
                a. Input
                    i. nums = [1,2,3], k = 3
                b. Output
                    i. 2
        3. Implementation
            - Summary
                a. While iterating over the array, store the sum of the values so far in the currSum
                variable while maintaining a dictionary with the key-value pairs being the index of
                the subarray and the sum of the values in the subarray.
            - Steps
                a. Initialize the dictionary using the collections.defaultdict(int) 
                class with a lambda function that returns 0.
                b. Initialize the res variable to 0 to store the amount of subarrays that are
                equivalent to k.
                c. Initialize the currSum variable to 0 to store the sum of the values so far.
        """
        # Dictionary to store number of subarrays
        # starting from index zero having 
        # particular value of sum.
        prevK = collections.defaultdict(lambda : 0)
    
        res = 0
    
        # k of elements so far.
        currsum = 0
    
        for i in range(0, len(nums)): 
    
            # Add current element to sum so far.
            currsum += nums[i]
    
            # If currsum is equal to desired sum,
            # then a new subarray is found. So
            # increase count of subarrays.
            if currsum == k: 
                res += 1        
    
            # currsum exceeds given sum by currsum - sum.
            # Find number of subarrays having 
            # this sum and exclude those subarrays
            # from currsum by increasing count by 
            # same amount.
            if (currsum - k) in prevK:
                res += prevK[currsum - k]
            
    
            # Add currsum value to count of 
            # different values of sum.
            prevK[currsum] += 1
        
        return res

print(subarrayk([1, 1, 1], 2))