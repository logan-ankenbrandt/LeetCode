from typing import List


def longestCommonPrefix(strs) -> str:
        """
        1. Goal
            - Find the longest commen prefix amongst a few arrays of strings.
        2. Examples
            - Example #1
                a. Input
                    i. strs = ["flower","flow","flight"]
                b. Output
                    i. "fl"
            - Example #2
                a. Input
                    i. strs = ["dog","racecar","car"]
                b. Output
                    i. ""
        3. Implementation
            - Summary
                1. Loop over the array of strings, create a zipped version of the strings
                to initialize the characters of interest, write a conditional statement that 
                checks the size of the set version of the tuples of interest to remove duplicates and ensures
                that it equals 1, append it to the list of common prefixes.
            - Steps
                1. Initialize an empty array to hold the longest common prefix
                2. Loop over the tuples in the zipped version of the string
                    i. zip() is a built-in function that creates an iterator, an object that 
                    presents the next value in the list, that will aggregate (in this case, the aggregation will be
                    the first elements of all the strings in the list up until the index of the shortest string) elements 
                    from two or more iteratables (in this case, the iterables are the strings in the list).
                    ii. *strs is used to generate a series of tuples containing elements (in this case, the first elements
                    of the strings in the list up to the index of the shortest string) from each iterable (the strings in the
                    list).
                3. Write a conditional statement that checks the size of the length of the
                set version of the zipped version of the string.
                    i. x is used to hold each element in the zipped version of the string.
                    ii. set() is used to remove all duplicates from x
                    iii. len() is used to get the length of the set version of x
                    iv. == 1 is used to ensure that every element that is appended to the prefix
                    array is consistent accross each string in the list.
                4. join the strings in the prefix array into a single string.
                5. Return the prefix string.
            - How I could have implemented this:
                1. What I knew:
                    - I knew that I needed to loop over the array in some capacity
                    - I knew that I needed to append the correct values to an array
                    - I knew that in order to combine the array values as a string,
                    I needed to use the join() method
                2. What I didn't know:
                    - I didn't know that I needed to use the zip() function to create an iterator
                    - I didn't know that I needed to use the set() function to remove duplicates
                    - I didn't know that I needed to use the len() function to get the length of the set 
                    version of the array
                    - I didn't know that I needed to use the == 1 condition to ensure that the iterable
                    was prevelant across the array
                3. What I can do next time:
                    - When you need to find similar values from a list of 
                    strings, use zip() and set() to remove duplicates and ensure that 
                    the iterable is prevelant
        """
        prefix=[]
        print(list(zip(*strs)))
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)

print(longestCommonPrefix(["dog","racecar","car"]))
