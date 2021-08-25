import itertools
from collections import Counter

def lengthOfLongestSubstring(self, s: str) -> int:
    """
    1. Goal
        - Find the longest substring without repeating characters
        and return its length
    2. Examples
        - Example #1
            a. Input
                i. s = "abcabcbb"
            b. Output
                i. 3
            c. Explanation
                i. The answer is "abc", with the length of 3.
        - Example #2
            a. Input
                i. s = "bbbbb"
            b. Output
                i. 1
            c. Explanation
                i. The answer is "b", with the length of 1.
        - Example #3
            a. Input
                i. s = "pwwkew"
            b. Output
                i. 3
            c. Explanation
                i. The answer is "wke", with the length of 3.
                Notice that the answer must be a substring,
                "pwke" is a subsequence and not a substring.
    3. Implementation
        - Issues
            a. How do I identify all of the substrings in a string with a
            hash table?
            b. How do I keep track of duplicates within substrings?
                ii. How can you go over the entire list of substrings
                to remove the substrings that contain duplicates?
                    - Currently, receiving an error when I try to remove
                    a substring from the substrings array
        - Steps
            a. Use itertools.combinations() within a for loop to find
            substrings and store it in a variable
            b. Use Counter() on each substring to identify duplicates
            c. Write a for loop to loop over the values in curr
            d. Write a conditional within the loop that checks if the value
            is greater than 1
                i. If it is, the string is appended to a duplicates list
            e. Write a for loop to loop over the substrings list
            f. Write a conditional within the loop that checks that the
            string is not in the duplicates list
                i. If it is not, the string is appended to the final list
            g. Find the length of the largest string within the final list
            h. Return the length of the largest string
        - Summary
            a. Used itertools.combinations() to identify all substrings,
            looped over the substrings list & created a dictionary with 
            the characters within the substring as the key and the number
            of times the character appears within the substring as the value,
            looped over the dictionary to add duplicate values to a list,
            looped over substrings again to find the substrings that had no
            duplicated, found the length of the largest string and returned its
            length.
        - Complexity Analysis
            a. Time Complexity: O(N^2)
                - Where N is the length of the string
            b. Space Complexity: O(N)
                - Where N is the length of the string
        - Is this optimized?
            a. No
    """
    if len(s) == 0:
            return 0
    substrings = []
    for x, y in itertools.combinations(range(len(s) + 1), r=2):
        substrings.append(s[x:y])
    duplicates = []
    for i in substrings:
        curr = Counter(i)
        for values in curr.values():
            if values != 1:
                duplicates.append(i)
    unique = []
    for i in substrings:
        if i not in duplicates:
            unique.append(i)
    m = max(unique, key=len)
    return len(list(m))
