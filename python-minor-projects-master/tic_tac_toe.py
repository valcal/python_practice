"""
TIC TAC TOE GAME
"""

#Game function

def game(x,o):
    round = 1
    win = 0
    example_board = [["   |   |   "], 
                     [" 7 | 8 | 9 "],
                     ["   |   |   "],
                     ["-----------"],
                     ["   |   |   "], 
                     [" 4 | 5 | 6 "],
                     ["   |   |   "],
                     ["-----------"],
                     ["   |   |   "], 
                     [" 1 | 2 | 3 "],
                     ["   |   |   "]]
    contents = ["blank", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    print("To type Your character in correct field, please type in field's corresponding number as shown below:")
    for verse in range(0, 11):
        print("".join(example_board[verse]))
    print("")
    print("Let's begin!")
    while win != 1:
        if contents[1] == contents[2] == contents[3] == "X" or contents[4] == contents[5] == contents[6] == "X" or contents[7] == contents[8] == contents[9] == "X" or contents[1] == contents[4] == contents[7] == "X" or contents[2] == contents[5] == contents[8] == "X" or contents[3] == contents[6] == contents[9] == "X" or contents[1] == contents[5] == contents[9] == "X" or contents[3] == contents[5] == contents[7] == "X":
            print("{} won!".format(x))
            break
        elif contents[1] == contents[2] == contents[3] == "O" or contents[4] == contents[5] == contents[6] == "O" or contents[7] == contents[8] == contents[9] == "O" or contents[1] == contents[4] == contents[7] == "O" or contents[2] == contents[5] == contents[8] == "O" or contents[3] == contents[6] == contents[9] == "O" or contents[1] == contents[5] == contents[9] == "O" or contents[3] == contents[5] == contents[7] == "O":
            print("{} won!".format(o))
            break  
        elif contents[1] != " " and contents[2] != " " and contents[3] != " " and contents[4] != " " and contents[5] != " " and contents[6] != " " and contents[7] != " " and contents[8] != " " and contents[9] != " ":
            print("It's a draw!")
            break
        if round % 2 == 0:
            print("{} turn!".format(o))
            while True:
                choice = input('Where do You want to put "O"?')
                if contents[int(choice)] == "O" or contents[int(choice)] == "X":
                    print("Please choose unoccupied field.")
                    print("")
                else:
                    break
            contents[int(choice)] = "O"
        elif round % 2 != 0:
            print("{} turn!".format(x))
            while True:
                choice = input('Where do You want to put "X"?')
                if contents[int(choice)] == "O" or contents[int(choice)] == "X":
                    print("Please choose unoccupied field.")
                    print("")
                else:
                    break
            contents[int(choice)] = "X"
        board = [["   |   |   "], 
                 [" {} | {} | {} ".format(contents[7], contents[8], contents[9])],
                 ["   |   |   "],
                 ["-----------"],
                 ["   |   |   "], 
                 [" {} | {} | {} ".format(contents[4], contents[5], contents[6])],
                 ["   |   |   "],
                 ["-----------"],
                 ["   |   |   "], 
                 [" {} | {} | {} ".format(contents[1], contents[2], contents[3])],
                 ["   |   |   "]]
        for verse in range(0, 11):
            print("".join(board[verse]))
        print("")
        round += 1

#Main function

print("Welcome to Tic Tac Toe Game!")
if input('Do You want to play game? (type "yes" if true)').lower() == 'yes':
    while True:
        player1 = input('Please enter Player 1 name:')
        player2 = input('Please enter Player 2 name:')
        chosen_character = input('Player One: Do You want to be "X" or "O"?').lower()
        if chosen_character == "x":
            x = player1
            o = player2
            print('{} will be first.'.format(x))
            print("")
        elif chosen_character == "o":
            x = player2
            o = player1
            print('{} will be first.'.format(x))
            print("")
        game(x,o)
        if input('Do You want to play again? (type "yes" if true)').lower() == "yes":
            continue
        else:
            print('Have a nice day!')
            break
else:
    print('Have a nice day!')
