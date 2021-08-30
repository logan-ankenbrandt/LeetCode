from typing import List
from collections import Counter
import re

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    """
        1. Goal
            - Return the most common word in a string that is not banned
        2. Examples
            - Example #1
                a. Input
                    i. paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",
                    banned = ["hit"]
                b. Output
                    i. "ball"
        3. Implementation
            - Steps
                a. Convert all of the characters in the paragraph string to
                lowercase and set it to the varaible p
                b. Use the re module to find only words in the p string
                c. Initialize a Counter() variable to count the frequency of words in the list
                d. Loop through the words in the banned array
                    i. If it is in the dictionary, delete it
                e. Return the key with the greatest value in the dictionary
            - Summary
                a. Use the re module to find only words, loop through a counter dictionary
                to remove the banned words, return the key with the greatest value
    """

    p = paragraph.lower()
    l = re.findall(r'[\w]+', p)
    c = Counter(l)
    for i in banned:
        if i in c:
            del c[i]
    return max(c, key=c.get)
