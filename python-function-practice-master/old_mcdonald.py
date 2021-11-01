"""
#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""

#old_macdonald('macdonald') --> MacDonald

def old_macdonald(name):
    new_name = ""
    count = 0
    for letter in name:
        if count != 2 and letter == name[0] or count != 2 and letter == name[3]:
            new_name += letter.capitalize()
            count += 1
        elif count == 2:
            new_name += letter
        else:
            new_name += letter
    return new_name
    
########## New Alternative code: ##########

def old_macdonald(name):
    new_name = name[0].capitalize() + name[1:3:1] + name[3].capitalize() + name[4::1]
    return new_name
