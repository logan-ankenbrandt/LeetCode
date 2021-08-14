def reverse(x) -> int:
        """
        1. Goal
            - Reverse the integers in a string
        2. Examples
            - Example #1
                a. Input
                    i. x = 123
                b. Output
                    i. 321
            - Example #2
                a. Input
                    i. x = -123
                b. Output
                    i. -321
            - Example #3
                a. Input
                    i. x = 120
                b. Output
                    i. 21
            - Example #4
                a. Input
                    i. x = 0
                b. Output
                    i. 0
        3. Implementation
            - Loop through the integer and append it to a list
            - Next:
                a. Loop through the list
                b. Write if statements to cover the edge cases
                c. Reverse the list
                d. Join the list into a string
                e. Return the string
            
        """
        
        integers = str(x)
        integers_list = []
        for i in integers:
            integers_list.append(i)


        
        if integers_list[0] == '0':
            return 0
        elif integers_list[0] == '-' and integers_list[-1] == '0':
            integers_list.pop(0)
            integers_list.reverse()
            while '0' in integers_list[0]:
                integers_list.remove('0')
            integers_list = ['-'] + integers_list
            integers = ''.join(integers_list)
        if integers_list[-1] == '0':
            integers_list.reverse()
            integers = ''.join(integers_list)
            integers = integers.strip('0')
        elif integers_list[0] == '-' and integers_list[-1] != '0':
            integers_list.pop(0)
            integers_list.reverse()
            integers_list = ['-'] + integers_list
            integers = ''.join(integers_list)
        elif len(integers_list) == 1:
            integers = integers_list[0]
        elif len(integers_list) == 10:
            return 0
        else:
            integers_list.reverse()
            integers = ''.join(integers_list)
        return integers

print(reverse(-901000))