"""
IS PANGRAM: Write a Python function to check whether a string is pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    for letter in alphabet:
        if letter in str1:
            continue
        else:
            return False
    return True
