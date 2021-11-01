"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
"""

#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    doll_text = ""
    for letter in text:
        doll_text += letter*3
    print(doll_text)
