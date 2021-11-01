"""
EVEN IN RANGE: Use range() to print all the even numbers from 0 to 10.
"""

for number in range(11):
    if number % 2 == 0:
        if number == 0:
            continue
        print(number)
