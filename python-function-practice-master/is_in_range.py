"""
IS IN RANGE: Write a function that checks whether a number is in a given range (inclusive of high and low)
"""

def ran_check(num,low,high):
    if num in range(low, high +1):
        print("{} is in the range between {} and {}".format(num,low,high))
    else:
        print("{} is not in the range between {} and {}".format(num,low,high))
        
######### Alternative ##########
        
def ran_bool(num,low,high):
    return num in range(low, high +1)
