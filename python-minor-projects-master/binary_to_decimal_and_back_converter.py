"""
Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
"""

print("Welcome to Binary to Decimal & Back converter!")
while True:
    action = input("Choose Your action:\n[1] - Convert binary to decimal\n[2] - Convert decimal to binary\n[3] - End program\n")
    if action == "1":
        number = input("Input binary number to convert:")
        print("Binary: {}, decimal: {}".format(number, int(number, 2)))
    elif action == "2":
        number = int(input("Input decimal number to convert:"))
        print("Decimal: {}, binary: {}".format(number, bin(number).replace("0b", "")))
    elif action == "3":
        print("You have chosen to end.")
        break
    else:
        print("Please type in correct action.")
