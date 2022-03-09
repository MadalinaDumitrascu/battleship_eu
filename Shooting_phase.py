def ask_shoot_coordinates(board):
    """it asks the player to give the coordinate on the basis of row,col. it validates the coordinate"""
    shoot = input("Now the fun starts!! Give the coordinate for the attack(ex. A2): ").upper()
    if len(shoot) != 2:
        shoot = input("Try again. Attack!!:(ex:A2): ").upper() 
    while not shoot[0].isalpha() or not shoot[1].isnumeric():
        shoot = input("Try again. Shoot!!:(ex:A2): ").upper()
    row, col = validate_shoot(board, shoot)
    return row, col

def validate_shoot(board, row, col):
    if board[row][col] == "#" or board[row][col] == "X":
        print("You have already shot a bullet there, pick another coordinate")


def shoot_ships(board, row, col):
    pass

"""it changes the 0 on the other player's board into M,H or S"""

def is_ship_sunk():
    pass
"""it checks if all the lenght of a ship has a H, and if it does it converts it so S"""

def display_boards():
    pass
"""it prints in the terminal both boards, with 0, M, H or S"""

def alternate_player():#asta cred ca o putem face si direct in main..?
    pass
"""after each shooting it alternates the player, and clearly indicates whose turn it is"""

def check_for_win():
    pass
"""after each turn check if all the X of each player have been changed to H or S"""
