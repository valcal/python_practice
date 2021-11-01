"""
LETTER CHANGING: Create a function that change letters of a string, making even letters small, and not-even letters big 
"""

def myfunc(string):
    number = 1
    string2 = ""
    for letter in string:
        if number % 2 == 0:
            string2 += letter.lower()
            number =- 1
        else:
            string2 += letter.upper()
            number += 1
    return str(string2)
