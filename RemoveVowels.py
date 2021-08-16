def removeVowels(s: str) -> str:
        """
        1. Goal
            - Remove all vowels from a string
        2. Example
            - Example #1 
                a. Input
                    i. s = "leetcodeisacommunityforcoders"
                b. Output
                    i. "ltcdscmmntyfcfgrs"
            - Example #2
                a. Input
                    i. s = "aeiou"
                b. Output
                    i. ""
        3. Implementation
            - Steps
                a. Initialize a list of the characters in the
                s string and a list of the vowels
                b. Iterate through the values in the vowels list,
                c. Write a while loop that will remove the vowels 
                while they are still in the vowels list
        """
        s_arr = list(s)
        vowels = list("aAeEiIoOuU")
        for vowel in vowels:
            while vowel in s_arr:
                s_arr.remove(vowel)
        return ''.join(s_arr)

print(removeVowels("leetcodeisacommunityforcoders"))