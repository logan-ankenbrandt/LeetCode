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
        count = 0
        number_list = []
        for i in s:
            if i == "I":
                count += 1
            elif i == "V":
                count += 5
            elif i == "X":
                count += 10
            elif i == "L":
                count += 50
            elif i == "C":
                count += 100
            elif i == "D":
                count += 500
            else:
                count += 1000
        return count