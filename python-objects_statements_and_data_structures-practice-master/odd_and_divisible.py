"""
ODD AND DIVISIBLE: Print which number is odd, and which is divisible by 5 from list below:

list1 = [1,2,3,4,5,6,7,8,9,10]
"""

list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    if num % 2 == 0:
        if num % 5 == 0:
            print('{} is dividable by 5'.format(num))
        else:
            print(num)
    else:
        if num % 5 == 0:
            print('{} is odd number and dividable by 5'.format(num))
        else:
            print('{} is odd number'.format(num))
