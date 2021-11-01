"""
UPPER VS LOWER: Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: .isupper() and .islower()
"""

def up_low(s):
    upper_char = 0
    lower_char = 0
    for letter in s:
        if letter.isupper():
            upper_char += 1
        if letter.islower():
            lower_char += 1
        else:
            continue
    print("No. of Upper case characters: {}".format(upper_char))
    print("No. of Lower case characters: {}".format(lower_char))
