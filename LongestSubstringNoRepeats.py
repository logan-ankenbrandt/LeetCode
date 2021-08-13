def lengthOfLongestSubstring(self, s: str) -> int:
        """
        1. Goal
            - Find the longest substring, so string within a string, without repeating characters.
        2. Examples
            - Example #1
                a. Input
                    i. s = "abcabcbb"
                b. Output
                    i. 3
                c. Explanation
                    i. The answer is "abc" with a length of 3
                    ii. In 'abca', there would be multiple 'a' values
            - Example #2
                a. Input
                    i. s = "bbbbb"
                b. Output
                    i. 1
                c. Explanation
                    i. The answer is "b" with a length of 1
            - Example #3
                a. Input
                    i. s = "pwwkew"
                b. Output
                    i. 3
                c. Explanation
                    i. The answer is "wke", with the length of 3.
                    Notice that the answer must be a substring, "pwke" is a 
                    subsequence and not a substring.
        3. Implementation
            - High-level
                a. Split the string into an array, and find out if a character equals another.
            - Low-level
                a. Split the string
                    i. Initialize an empty "string_list"
                    ii. Iterate through the string
                    iii. Append each value from the string to the list
                b. Initialize a count
                c. Compare values
        4. Issues:
            - Having issues comparing values:
                a. Currently, this function creates an array of 
                duplicates and counts the amount of items in that 
                array.
                b. I need to initialize a count value, start comparing
                the values at the beginning of the list, increment the count for
                each value that has not been seen, stop the count when a duplicate is found,
                and initialize a new count when a non-duplicate is found. 
        """
        string_list = []
        for i in s:
            string_list.append(i)
    
        duplicates = []
        for i in string_list:
            if i not in duplicates:
                duplicates.append(i)
            else:
                duplicates = duplicates
        return len(duplicates)