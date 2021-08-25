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
                a. Initialize the sub variable & set it to an empty dict to
                keep track of:
                    i. The characters in the substring
                    ii. The characters index
                    iii. and as the data structure that the loop compares
                    the current element against to know if it is to:
                        - Keep moving forward
                        - Stopping, performing the size calculations, and
                        resetting the starting point to the current index
                b. Initialize the start variable to:
                    i. Keep track of what index the loop needs to start from
                    ii. Be reset to the current index when a duplicate is found
                c. The size variable to keep track of the substrings length
                d. The longest variable to return the longest substring
                e. Write a for loop that:
                    i. Sets the i variable to track the index
                    ii. Sets the letter variable to track the characters
                    iii. Uses the enumerate() function over the string to
                    keep track of the index & store it in i
                f. Write a conditional that checks if:
                    i. The letter is in the dictionary (as a key) 
                    ii. The the value of the key is greater than the start
                    iii. We've seen the character at an index that is within
                    the current substring
                g. Within the conditional, write a statement that:
                    i. Resets the start of the next substring at the index
                    of the duplicate plus one
                    ii. Sets the length of the current size to the current
                    index subtracted from the index position of the duplicate
                    iii. Set the previous start index to the current character
                h. Write a catch-all statement (else statement) that:
                    i. Adds the letter to the dictionary if it hasn't been
                    seen before.
                    ii. Addes the letter to the dictionary if it has been seen
                    before but it was before the index of our substring
                    iii. Add one to the current size
                i. Write a conditional within the previous else statement that:
                    i. Checks if the size of the current substring is longer than
                    the longest substring so far.
                    ii. Sets the longest size to the current one if so
            - Summary
                i. Initialize a dictionary to track the characters in the string & 
                their index, initialize a start variable & set to 0 in order to keep 
                track of the beginning of the current substring, initialize the size
                variable & set it to 0 to track the size of the current substring,
                initialize the longest & set it to 0 to track the longest substring so
                far, write a for loop that loops over an enumerated version of the string,
                write a conditional that checks the letter is in the dictionary or if the
                character was seen within the index of the string, and compare the size
                of the current substring in order to update the longest variable if 
                necessary.
        """
        
        sub = {}
        start = 0
        size = 0
        longest = 0
        
        for i, letter in enumerate(s):
            if letter in sub and sub[letter] >= start:
                start = sub[letter] + 1
                size = i - sub[letter]
                sub[letter] = i
            else:
                sub[letter] = i
                size += 1
                if size > longest:
                    longest = size
        
        return longest