"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
"""

#spy_game([1,2,4,0,0,7,5]) --> True
#spy_game([1,0,2,4,0,5,7]) --> True
#spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    index = 0
    suspects = []
    for number in nums:
        if number == 0 or number == 7:
            suspects.append(number)
    if suspects == [0, 0, 7]:
        return True
    else:
        return False
