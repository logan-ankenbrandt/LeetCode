from typing import List
import snoop

@snoop
def highFive(self, items: List[List[int]]) -> List[List[int]]:
        """
        1. Goal
            - Calculate the students top 5 averages
        2. Examples
            - Example #1
                a. Input
                    i. items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
                b. Output
                    i. [[1,87],[2,88]]
            - Example #2
                a. Input
                    i. items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
                b. Output
                    i. [[1,100],[7,100]]
        3. Implementation
            - Summary
                a. Initialize a dictionary, store each unique key in the dictionary and set its value to a list
                of the keys values, write a function that finds the average of the list, loop over the dictionary
                and run the sort_avg function on each key-value pair to find the average for each variable,
                append the key-value pairs to the final list as a tuple
            - Steps
                a. Initialize an empty dictionary
                b. Loop over the list of lists
                c. Write a conditional statement that states:
                    i. If the first element of the list of lists is in the
                    dictionary, append the second element of the list of lists 
                    to the key, which is the first element, stored in the dictionary
                        - This will add the values as a list to the dictionary
                        with the key being the first number in the list of lists
                    ii. Else, insert the key in the dictionary using dictionary[item[]0]
                    and set it equal to the second element of the list of lists
                d. Initialze an empty list to store the result
                e. Write a sort average function that 
                    i. Sorts the list in reverse order to get the values from 
                    greatest to least
                    ii. Finds the sum of the top 5 values and divides it by 5
                f. Loop over the dictionary and
                    i. append the key to the final list and run the sort_average
                    function on each key-value pair in the dictionary to return the
                    average
                g. Return the sorted final list
        """
        v = {}
        for i in items:
            if i[0] in v:
                v[i[0]].append(i[1])
            else:
                v[i[0]] = [i[1]]
        
        final = []

        def sort_avg(list):
            list = sorted(list, reverse = True)
            return int(sum(list[:5]) / 5)

        for i in v:
            final.append([i, sort_avg(v[i])])
        return sorted(final)

print(highFive(highFive, [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))