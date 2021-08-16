from typing import List


def fizzBuzz(self, n: int) -> List[str]:
        """
        1. Goal
            - For every value in a list of (n) length, change the
            value to "Fizz", "Buzz", or "FizzBuzz" depending on the numbers
            divisibility by 3 and 5
        2. Examples
            - Example #1
                a. Input
                    i. n = 3
                b. Output
                    i. ["1","2","Fizz"]
            - Example #2
                a. Input
                    i. n = 5
                b. Output
                    i. ["1","2","Fizz","4","Buzz"]
            - Example #3
                a. Input
                    i. n = 15
                b. Output
                    i. ["1","2","Fizz","4","Buzz","Fizz","7",
                    "8","Fizz", "Buzz","11","Fizz","13","14",
                    "FizzBuzz"]
        3. Implementation
            - Summary
                a. Initialize an empty list using the range of n,
                loop through the range of n + 1 starting at index 1,
                set variables equal to the divisibility of the iterable
                by 3 and 5, append the appropriate value to the empty list
                if it equals the conditions of interest.
            - Steps
                a. Initialize an empty list
                b. Loop through the range of n + 1 starting at index 1
                c. In the loop, set variables equal to the divisibility of
                3 and 5
                c. Write conditional statements for
                    i. If the integer of i is divisible by 3
                    but not 5
                    ii. If the integer of i is divisible by 5
                    but not 3
                    iii. If the integer of i is divisible by 
                    3 and 5
                    iv. Otherwise, return the i
        """
        ans = []
        for num in range(1, n+1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(num))
        return ans