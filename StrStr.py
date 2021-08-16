def strStr(self, haystack: str, needle: str) -> int:
    """
    1. Goal
        - Find the index of the first occurrence of needle 
        in haystack, or -1 if needle is not part of haystack.
    2. Examples
        - Example #1
            a. Input: 
                i. haystack = "hello", needle = "ll"
            b. Output: 2
        - Example #2
            a. Input:
                i. haystack = "aaaaa", needle = "bba"
            b. Output: -1
    3. Implementation
        - Summary
            - Use the find method on the haystack with needle
            as the parameter.
        - Steps
            - haystack.find(needle)
    """
    return haystack.find(needle)