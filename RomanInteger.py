def romanToInt(self, s: str) -> int:
    """
    1. Goal
        - Convert an Roman numeral to an integer
    2. Examples
        - Example #1
            a. Input
                i. s = "III"
            b. Output
                i. 3
        - Example #2
            a. Input
                i. s = "IV"
            b. Output
                i. 3
        - Example #3
            a. Input
                i. s = "IX"
            b. Output
                i. 9
        - Example #4
            a. Input
                i. s = "LVIII"
            b. Output
                i. 3
                58
            c. Explanation
                L = 50, V = 5, III = 3
    3. Implementation
        - Initialize a count
        - Initialize a for loop
            a. For each element in the string, if the element equals
            a numeral, convert it to a number and add it to the count
    4. Issues
        - I can't figure out how to handle the "IV" case
    """
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    count = 0
    """
    The count variable is initialized to keep track of the
    sum of the Roman characters.
    """
    i = 0
    """
    The i variable is used to keep track of what index the pointer is iterating on.
    """
    while i < len(s):
        """
        The while loop iterates through the string, checking if:
            a. The current element is a numeral
            b. The current element is greater than or less than the previous element
            c. If the index is greater than the length of the string, the loop is broken
        """
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            """
            Things going on here:
                a. The statement 'if i + 1 < len(s)' ensures that the index is not
                greater than the length of the string.
                b. The statement 'values[s[i]] < values[s[i + 1]]' ensures that the
                current element is less than the next element.
            """
            count += values[s[i + 1]] - values[s[i]]
            """
            This statement subtracts the value of the next element from the current 
            element.
            Example:
                a. If the current element is 'I' and the next element is 'V', then the resulting
                operation is '5 -1 - 4'
            """
            i += 1
            """
            1 is added to the index to ensure that the loop is properly indexed.
            """
        else:
            """
            Basically, in any scenario other than when the next element
            is greater than the current element, the current value is simply added
            to the count.
            """
            count += values[s[i]]
            i += 1
    
    return count