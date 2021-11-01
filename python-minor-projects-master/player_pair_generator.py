"""
Player Pair Generator
Revision: 15.02.2020
Developed by: Marcin Mierzejewski

A simple code, that allows to generate pairs from given player base, in tournament style. 
Players can be typed-in or imported from .txt file.
Pairs can be generated with exceptions (Player 1 cannot play with Player 2 etc.)
Results can be inported to .txt file.
"""

from random import randint

finish = 0
generated = 0
pairs_generated = 0


# Player Object declaration

class Player:

    def __init__(self, name):
        self.name = name
        self.exceptions = []

    def add_exceptions(self, exception):
        self.exception = exception
        self.exceptions.append(exception)


# Function responsible for filling in given players and their exceptions

def define_players_with_exceptions(number_of_players, number_of_exceptions):
    player_list = []
    for number in range(1, number_of_players + 1):
        print("\n")
        player = (input("Type in name of player nr {}:".format(number)))
        player = Player("{}".format(player))
        player_list.append(player)
        for number2 in range(1, number_of_exceptions + 1):
            print("\n")
            player.add_exceptions(input("Type in name of exception nr {}:".format(number2)))
    print("\n")
    print("Here is Your list of players and exceptions for them:")
    print("\n")
    for number in range(0, len(player_list)):
        print("Player no. {}: {}, exceptions: {}".format(number + 1, player_list[number].name, player_list[number].exceptions))
    print("\n")
    return player_list


# Function responsible for importing players and their exceptions from defined text file

def read_player_base_file():
    player_list = []
    f = open("player base.txt", "r")
    f1 = f.readlines()
    for x in f1:
        player_exceptions_separation = x.split(" - ")
        player = player_exceptions_separation[0]
        player = Player("{}".format(player))
        player_list.append(player)
        exceptions = player_exceptions_separation[1].split(", ")
        for number in range(0, len(exceptions)):
            player.add_exceptions(exceptions[number])
    f.close()
    print("\n")
    print("Player list and their exceptions imported!")
    print("Here is Your list of players and exceptions for them:")
    print("\n")
    for number in range(0, len(player_list)):
        print("Player no. {}: {}, exceptions: {}".format(number + 1, player_list[number].name, player_list[number].exceptions))
    print("\n")
    number_of_players = len(player_list)
    return [player_list, number_of_players]


# Function responsible for generating pairs, considering their exceptions

def generate_player_pairs(player_list, number_of_players):
    players_generated = []
    generated = 0
    number = 1
    pair_list = []
    print("\n")
    print("Generated player pair:")
    while generated != int(number_of_players / 2):
        player1 = randint(0, number_of_players - 1)
        player2 = randint(0, number_of_players - 1)
        if player1 != player2 and not (player1 in players_generated) and not (player2 in players_generated) and not (
                player_list[player1].name in player_list[player2].exceptions) and not (
                player_list[player2].name in player_list[player1].exceptions):
            print("Pair no. {}: {} vs {}".format(number, player_list[player1].name, player_list[player2].name))
            pair_list.append("Pair no. {}: {} vs {}".format(number, player_list[player1].name, player_list[player2].name))
            players_generated.append(player1)
            players_generated.append(player2)
            generated += 1
            number += 1
        else:
            continue
    print("\n")
    return pair_list


# Function responsible for exporting player paris to text file

def export_to_file(pair_list):
    f = open("player pairs.txt", "w+")
    for i in range(len(pair_list)):
        f.write("{}".format(pair_list[i]))
        f.write("\n")
    f.close()
    print("\n")
    print("Player pairs exported!")
    print("\n")


# Main block with menu

print("Welcome to the Player Pair Generator!")
print("\n")
while finish != 1:
    print("Menu:")
    print("[1] Define players with exceptions")
    print("[2] Import players from defined file")
    print("[3] Generate player pairs")
    print("[4] Export player pairs list to file")
    print("[5] Finish")
    print("\n")
    decision = int(input("Choose what You want to do:"))
    if decision == 1:
        number_of_players = int(input("How many players there will be?"))
        number_of_exceptions = int(input("How many exceptions for each player there will be?"))
        player_list = define_players_with_exceptions(number_of_players, number_of_exceptions)
        generated = 1
    elif decision == 2:
        result = read_player_base_file()
        player_list = result[0]
        number_of_players = result[1]
        generated = 1
    elif decision == 3:
        if generated == 0:
            print("\n")
            print("ERROR - You need to determine players and their exceptions in order to generate pairs.")
            print("\n")
            continue
        pair_list = generate_player_pairs(player_list, number_of_players)
        pairs_generated = 1
    elif decision == 4:
        if pairs_generated == 0:
            print("\n")
            print("ERROR - You need to generate pairs in order to export them to text file!.")
            print("\n")
            continue
        export_to_file(pair_list)
    elif decision == 5:
        print("\n")
        print("You have chosen to finish.")
        finish = 1
        break
    else:
        print("\n")
        print("Please choose correct option from menu.")
        print("\n")
