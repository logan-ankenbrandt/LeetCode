from typing import List


def plusOne(digits: List[int]) -> List[int]:
        """
        1. Goal
            - Add one to a list of digits, and return
            a list of the new digits.
        2. Examples
            - Example #1
                a. Input: 
                    i. [1, 2, 3]
                b. Output:
                    i. [1, 2, 4]
            - Example #2
                a. Input: 
                    i. [9, 9]
                b. Output:
                    i. [1, 0, 0]
        3. Implementation
            - Summary
                a. Convert the list of digits to a single digit, 
                add one, and convert the result back to a list.
            - Steps
                a. Convert the list of digits to a list of strings.
                b. Conver the list of stings to a single string.
                c. Convert the single string to an integer.
                d. Add one to the integer.
                e. Convert the integer back to a string.
                f. Convert the string back to a list of integers.
        """
        strings = [str(integer) for integer in digits]
        a_string = "".join(strings)
        an_integer = int(a_string)
        final_value = an_integer + 1
        string_again = str(final_value)
        splitted = string_again.split()
        integers = [int(integer) for integer in string_again]
        return integers
print(plusOne([1, 2, 3]))