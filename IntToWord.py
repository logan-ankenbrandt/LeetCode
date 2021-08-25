def numberToWords(self, num: int) -> str:
    """
    1. Goal
        a. Convert a number to it's english representation
    2. Examples
        - Example #1
            a. Input
                i. num = 123
            b. Output
                i. "One Hundred Twenty Three"
            c. Explanation
                i. 123 -> "Hundred"
                ii. 1.2.3 -> "One Hundred"
                iii. 2.3 -> "Twenty" -> "One Hundred Twenty"
                iv. 3 -> "Three" -> "One Hundred Twenty Three"
        - Example #2
            a. Input
                i. num = 12345
            b. Output
                i. "Twelve Thousand Three Hundred Forty Five"
        - Example #3
            a. Input
                i. num = 1234567
            b. Output
                i. "One Million Two Hundred Thirty Four Thousand
                Five Hundred Sixty Seven"
        - Example #4
            a. Input
                i. num = 1234567891
            b. Output
                i. "One Billion Two Hundred Thirty Four Million
                Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    3. Implementation
        - Issues
        - Steps
            a. Define one() that:
                i. Takes num as a param
                ii. Returns the english representation of num by searching a 
                dictionary for it's key-value pair.
            b. Define two_less_20() that:
                i. Takes num as a param
                ii. Returns the english representation of num by searching a 
                dictionary for it's key-value pair.
            c. Define ten() that:
                i. Takes num as a param 
                ii. Returns the english representation of num by searching a 
                dictionary for it's key-value pair.
            d. Define two() that:
                i. Takes num as a param
                ii. Has a conditional that:
                    - Ensures that num is an int
                    - Passes the num through the one funciton if it
                    is less than 10
                    - Passes the num through the two_less_20 function if it
                    is less than 20
                    - Otherwise,
                        a. Divide num by 10 & set to variable
                        b. Subtract num by variable & multiply by 10
                        c. 
        - Summary
    """
    def one(num):
        switcher = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
        }
        return switcher.get(num)


    def two_less_20(num):
        switcher = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return switcher.get(num)


    def ten(num):
        switcher = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return switcher.get(num)


    def two(num):
        if not num:
            return ''
        elif num < 10:
            return one(num)
        elif num < 20:
            return two_less_20(num)
        else:
            tenner = num // 10
            rest = num - tenner * 10
            return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)


    def three(num):
        hundred = num // 100
        rest = num - hundred * 100
        if hundred and rest:
            return one(hundred) + ' Hundred ' + two(rest)
        elif not hundred and rest:
            return two(rest)
        elif hundred and not rest:
            return one(hundred) + ' Hundred'
        
        billion = num // 1000000000
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        if not num:
            return 'Zero'

        result = ''
        if billion:
            result = three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result
