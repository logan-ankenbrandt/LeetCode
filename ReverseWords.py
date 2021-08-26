def reverseWords(self, s: str) -> str:
    """
    1. Goal
        - Reverse the words in a string
    2. Example
        - Example #1
            a. Input
                i. s = "Let's take LeetCode contest"
            b. Output
                i. "s'teL ekat edoCteeL tsetnoc"
    3. Implementation
        - Steps
            a. Initialize an empty list to store the reversed words
            b. Loop through the splitted string
            c. Append the reversed strings to the list
            d. Return the joined list
    """
    
    p = []
    for i in s.split(" "):
        p.append(i[::-1])
    return ' '.join(p)
