import snoop

@snoop
def areOccurrencesEqual(s: str) -> bool:
        """
        1. Goal
            - Return true if all the characters in the string
            have the same occurences
        2. Examples
            - Example #1
                a. Input
                    i. s = "abacbc"
                b. Output
                    i. True
            - Example #2
                a. Input
                    i. s = "aaabb"
                b. Output
                    i. False
        3. Implementation
            - Summary
                a. Iterate over the string, write a conditional                       
                statement that checks if the character is in the 
                dictionary, add it to the dictionary if it is and
                add one, else add one to its current value
            - Steps
                a. Create a hash table
                b. Loop over the characters in the string
                c. If the character is not in the hash table,
                store it as the key and add 1 to its value
                d. If the character is in the hash table, add one
                to its value
                e. Set the default result to True
                f. Initialze the val variable and set it to the
                0 value of the dictionary (this will be used to 
                iterate through the dictionary)
                g. Loop through the values in the dictionary
                h. Write a conditional statement to check if the
                current value in the dictionary is not equal to the 
                rest of the values

        """
        v = {}
        for i in list(s):
            if i not in v:
                v[i] = 1
            else:
                v[i] += 1
        res = True
        val = list(v.values())[0]
        for ele in v:
            if v[ele] != val:
                res = False
        return res

print(areOccurrencesEqual('abacbd'))