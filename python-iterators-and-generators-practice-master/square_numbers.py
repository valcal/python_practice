"""
Iterators and Generators Homework
Problem 1

SQUARE NUMBERS: Create a generator that generates the squares of numbers up to some number N.

def gensquares(N):

    pass

for x in gensquares(10):
    print(x)
"""

def gensquares(N):
    for number in range(N):
        yield number**2
        
for x in gensquares(10):
    print(x)
