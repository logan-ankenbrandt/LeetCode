from typing import List
import snoop

@snoop
def maximumWealth(accounts: List[List[int]]) -> int:
        """
        1. Goal
            - Iterate through a list of lists to find the 
            greatest sum
        2. Examples
            - [[1,2,3],[4,5,6],[7,8,9]] -> 15
        3. Implementation
            - Initiailze an empty list to store the 
            sum of the lists
            - Iterate through the list of lists
            - Append the sum of the lists to the list
            - Return the max of the list
        """
        res = []
        for i in accounts:
            res.append(sum(i))
        return max(res)

print(maximumWealth([[1,2,3],[4,5,6],[7,8,9]]))