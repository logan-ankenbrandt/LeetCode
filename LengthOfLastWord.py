def lengthOfLastWord(self, s: str) -> int:
        """
        1. Goal
            - Return the length of the last word in the string s.
        2. Examples
            - lengthOfLastWord("Hello World") → 5
            - lengthOfLastWord("Hello World   ") → 5
        3. Implementation
            - Split the string into a list of words.
            - Set a value to an empty string.
            - Write a while loop that deletes the empty string
            while it is still in the list.
            - Return the length of the last word in the list.
        """
        s_array = s.split(" ")
        val = ""
        while val in s_array:
            s_array.remove(val)
        return len(s_array[-1])