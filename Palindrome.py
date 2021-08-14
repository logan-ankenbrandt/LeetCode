def isPalindrome(self, x: int) -> bool:
        """
        1. Goal
            - Check if a number reads the same backwards as forwards
        2. Examples
            - Example #1
                a. Input
                    i. x = 121
                b. Output
                    i. True
            - Example #2
                a. Input
                    i. x = -121
                b. Output
                    i. False
        3. Implementation
            - Convert x to a list
            - Reverse the list
            - Join the list into a string
            - Convert the string to an int
            - Check if the int is equal to x
        """
        
        palindrome = []
        x = str(x)
        for i in x:
            palindrome.append(i)
        
        if palindrome[0] == '-':
            return False
        
        palindrome.reverse()
        palindrome = "".join(palindrome)
        palindrome = int(palindrome)
        if palindrome == int(x):
            return True
        else:
            return False