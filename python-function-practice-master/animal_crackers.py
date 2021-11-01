"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
"""

#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    text_list = text.split()
    if text_list[0][0] == text_list[1][0]:
        return True
    else:
        return False
