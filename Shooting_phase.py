import Placing_phase

def ask_shoot_coordinates(board):
    """it asks the player to give the coordinate on the basis of row,col. it validates the coordinate"""
    coordinate = input("Now the fun starts!! Give the coordinate for the attack(ex. A2): ").upper()
    if len(coordinate) != 2:
        coordinate = input("Try again. Attack!!:(ex:A2): ").upper() 
    while not coordinate[0].isalpha() or not coordinate[1].isnumeric():
        coordinate = input("Try again. Shoot!!:(ex:A2): ").upper()
    shot_row, shot_col = Placing_phase.validate_coordinates(board, coordinate)

    return shot_row, shot_col

# def validate_shoot(board, shoot):
#     row, col = Placing_phase.validate_coordinates(board, shoot)
#     if board[row][col] == "M" or board[row][col] == "X":
#         print("You have already shot a bullet there, pick another coordinate")
#         ask_shoot_coordinates(board)
#     else:
#         None


# def shoot_ships(board, row, col):
#     pass

#     """it changes the 0 on the other player's board into M,H or S"""

def is_ship_sunk(enemy_board, lenght_ship):
    """it checks if all the lenght of a ship has a H, and if it does it converts it so S
    00xx
    x000
    x000"""
    count_hit = 0
    for row in enemy_board: 
        if row == "H": 
            count_hit = count_hit + 1



def display_boards():
    pass
    """it prints in the terminal both boards, with 0, M, H or S"""

# def alternate_player():#asta cred ca o putem face si direct in main..?
#     pass
#     """after each shooting it alternates the player, and clearly indicates whose turn it is"""

# def check_for_win():
#     pass
#     """after each turn check if all the X of each player have been changed to H or S"""
