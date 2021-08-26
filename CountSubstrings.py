import itertools
import snoop

@snoop
def countSubstrings(s: str) -> int:
    """
    1. Goal
        - Count the number of substrings that are palindromes.
    2. Examples
        - Example #1
            a. Input
                i. "abc"
            b. Output
                i. 3
            c. Explanation
                - The palindromes are "a", "b", and "c".
    3. Implementation
        - Steps
            a. Initialize a count variable
            b. Loop over the indexes of the string
            c. Set two variables, left and right, to the indexes
            d. Write a function that:
                i. Contains a while loop that:
                    - Runs while 
                        a. Left is greater than 0 and right is less 
                        than the length of the string
                        b. And the value at the left index is equal to 
                        the value at the right index
                        c. This ensures that it is a palindrome
                    - Increments the count variable by 1
                    - Decrements left variable to the left by 1 
                        a. This is to ensure that the left index
                        is always less than the right index 
                    - Increments right variable to the right by 1
                i. Set the l variable to the index and set the r variable 
                to the index plus one
            e. Return the count variable
        - Summary
            a. Each char in str as middle and expand outwards, 
            do same for pali of even len; maybe read up on manachers 
            alg
    """
    count = 0

    for i in range(len(s)):
        count += countPalindrome(s, i, i)
        count += countPalindrome(s, i, i + 1)
    return count

def countPalindrome(s, l, r):
    count = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        count += 1
        l -= 1
        r += 1
    return count

print(countSubstrings("abc"))
