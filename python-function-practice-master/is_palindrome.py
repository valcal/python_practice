"""
IS PALINDROME: Write a Python function that checks whether a passed in string is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
"""

s = input("Enter a sequence to check, if it's a palindrome.")
char_group = [" ", "!", "?", ".", ","]
s_new=s
for symbol in char_group:
    s_new = s_new.replace("{}".format(symbol), "")
if s_new.lower() == s_new[::-1].lower():
    print("It's a palindrome!")
    print(s_new.lower())
else:
    print("It's not a palindrome!")
    if len(s_new) % 2 == 0:
        upper_range = len(s_new)//2
    else:
        upper_range = len(s_new)//2 +1
    for number in range(0, upper_range):
        if s_new.lower()[number] != s_new.lower()[-(number + 1)]:
            print(s_new.lower())
            print("Difference between " + s_new.lower()[number] + " and " + s_new.lower()[-(number + 1)])
        else:
            continue
