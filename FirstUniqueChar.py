from collections import Counter

def firstUniqueChar(s: str) -> int:
        """
        1. Goal
            a. Find the first non-repeating character in a string
            and return its index
        2. Examples
            a. Example #1
                a. Input
                    i. s = "leetcode"
                b. Output
                    i. 0
            a. Example #2
                a. Input
                    i. s = "loveleetcode"
                b. Output
                    i. 2
        3. Implementation
            a. Summary
                i. Use counter to count the number of each 
                character in a string, loop through the dict,
                return the index of the first key that equalst
                the value of 1.
            b. Steps
                i. Create a dictionary of the string 
                using Counter()
                ii. Loop through the dictionary items
                iii. If the value of the key is 1, 
                return the key
                iv. Otherwise, return -1

        """
        
        counted = Counter(s)
        for key, value in counted.items():
            if value == 1:
                return s.index(key)
        return -1

print(firstUniqueChar("loveleetcode"))