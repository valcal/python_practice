"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
"""

#summer_69([1, 3, 5]) --> 9
#summer_69([4, 5, 6, 7, 8, 9]) --> 9
#summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    index = 0
    left_border = 0 
    right_border = 0
    for number in arr:
        if number == 6:
            left_border = index
            index += 1
        elif number == 9:
            right_border = index +1
            index += 1
        else:
            index += 1
    new_arr = arr[left_border:right_border]
    score = sum(arr) - sum(new_arr)
    return score
