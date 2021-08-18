from typing import List
import snoop

@snoop
def countConsistentStrings(allowed: str, words: List[str]) -> int:
        """
        1. Goal
            - Count the number of strings in a list where
            only the allowed elements appear
        2. Examples
            - Example #1
                a. Input
                    i. allowed = "ab", 
                    words = ["ad","bd","aaab","baa","badab"]
                b. Output
                    i. 2
            - Example #2
                a. Input
                    i. allowed = "abc", 
                    words = ["a","b","c","ab","ac","bc","abc"]
                b. Output
                    i. 7
        3. Implementation
            - Summary
                a. Loop over words and check if the length of 
                the characters in words subtracted by the length
                of the allowed characters is equal to 0, if so,
                add to count
            - Steps
                a. Initialize count to 0
                b. Set the allowed string to a set
                c. Loop over words
                d. Write a conditional that checks:
                    i. If the length of the characters in the
                    word set subtracted by the allowed set is equal
                    to 0
                        - If so, add to count
                e. Return count
        """
        
        allowed = set(allowed)
        count = 0
        curr_count = 0
        for i in words:
            if len(set(i) - allowed)  == 0:
                count += 1
            else:
                curr_count = len(set(i) - allowed)
                print(curr_count)
        return count

print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))