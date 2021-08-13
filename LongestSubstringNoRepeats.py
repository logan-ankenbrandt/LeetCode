def lengthOfLongestSubstring(s) -> int:
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
            - Brute Force
                a. Summary
                    i. Enumerate all possible substrings, check if the substring has repeating
                    characters, and return the longest substring without repeating characters.
                b. Steps
                    i. Get the length of the string for indexing
                    ii. Within two for loops:
                        a. Initialize the index of the string with the length you
                        attained earlier
                        b. Use the for loops to create seperate variables to compare substrings
                        against.
                        c. Define a check function to check for duplicates within every possible substrings
                            i. Set a chars variable to be an empty list with every possible
                            characters that could be in the string
                            ii. Loop through the start and end of every substring, acquired as
                            the variables attained in the two previous for loops, to 
                                - List out all possible substrings and set it to the variable "c".
                                - Keep count of the number of occurences of each character in the substring, i.e. counting 
                                duplicates, by using the ord() function to convert each character to its ASCII value.
                        d. Return the length of the longest substring by using the max() function

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
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                """
                This loop is used to list all possible substrings
                """
                c = s[i]
                """
                The c variable is used to list out all substrings
                """
                chars[ord(c)] += 1
                """
                The above statement is used to keep count of the number of occurences of each
                character in each substring.
                ord() is used to convert the character to its ASCII value - used to check for
                duplicates.
                """
                if chars[ord(c)] > 1:
                    """
                    If there are no duplicates, return false
                    """
                    return False
            return True
            """
            Default is that there are duplicates, so it is set to true
            """
        
        n = len(s)
        res = 0

        for i in range(n):
            """
            i == index of array
            """
            for j in range(i, n):
                """
                j == the iterative index of array
                j is the value that is creating all of the substrings
                """
                if check(i, j):
                    """
                    If check returns true, then perform the below operations
                    """
                    res = max(res, j - i + 1)
                    """
                    Sets the maximum value to this variable with the max() function
                    """
        return res

print(lengthOfLongestSubstring("abcabcbb"))