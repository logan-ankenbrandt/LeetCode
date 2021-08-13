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
            
        """
        
        integers = str(x)
        integers_list = []
        for i in integers:
            integers_list.append(i)
            
        

        for i in integers_list:
            if integers_list[0] == '-':
                integers_list.pop(0)
                integers_list.reverse()
                integers_list = ['-'] + integers_list
                integers = ''.join(integers_list)
            elif integers_list[-1] == '0':
                integers_list.pop()
                integers_list.reverse()
                integers = ''.join(integers_list)
                print(integers)
            elif len(integers_list) == 1:
                integers = ''.join(integers_list)
            else:
                integers_list.reverse()
                integers = ''.join(integers_list)
        return integers

print(reverse(120))