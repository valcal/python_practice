"""PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter

print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *

HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
For purposes of this exercise, it's ok if your dictionary stops at "E".
"""

def print_big(letter):
    representations = {"a":[[" ", " ", "*", " ", " "],[" ", "*", " ", "*", " "],["*", "*", "*", "*", "*"],["*", " ", " ", " ", "*"],["*", " ", " ", " ", "*"]],"b" :[["*", "*", "*", "*", " "],["*", " ", " ", " ", "*"], ["*", "*", "*", "*", " "], ["*", " ", " ", " ", "*"], ["*", "*", "*", "*", " "]], "c" : [[" ", "*", "*", "*", "*"], ["*", " ", " ", " ", " "], ["*", " ", " ", " ", " "], ["*", " ", " ", " ", " "], [" ", "*", "*", "*", "*"]], "d" : [["*", "*", "*", "*", " "], ["*", " ", " ", " ", "*"], ["*", " ", " ", " ", "*"], ["*", " ", " ", " ", "*"], ["*", "*", "*", "*", " "]], "e" : [["*", "*", "*", "*", "*"], ["*", " ", " ", " ", " "], ["*", "*", "*", "*", "*"], ["*", " ", " ", " ", " "], ["*", "*", "*", "*", "*"]]}
    for u,w,x,y,z in representations[letter]:
        print(u,w,x,y,z)
