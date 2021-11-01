"""
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
"""

#count_primes(100) --> 25

#By convention, 0 and 1 are not prime.

def count_primes(num):
    score = 0
    for number in range(2, num + 1):
        divisions = 0
        for division in range(1, number + 1):
            if number % division == 0:
                divisions += 1
        if divisions == 2:
            score += 1
            
    return score
