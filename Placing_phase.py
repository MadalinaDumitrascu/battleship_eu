import random


def get_board_size():
    admitted_size = ["5", "6", "7", "8", "9", "10"]
    print("Let's choose the board now!!")
    row = input("Give us the width of the board(between 5-10): ")
    while not row.isnumeric() or not row in admitted_size:
        row = input("Try again. It must be a number from 5 to 10: ")
    col = input("Type also the height of the board: ")
    while not col.isnumeric() or not col in admitted_size:
        col = input("Try again. It must be a number from 5 to 10: ")
    return int(row), int(col)

def start_menu():
    valid_mode = ["1", "2"]
    game_mode = input("choose game mode: 1 - PvP; 2 - PvAi: ")
    while not game_mode in valid_mode:
        game_mode = input("try again. 1 or 2: ")    
    rows, cols = get_board_size()

    return game_mode, rows, cols   

def create_board(rows, cols):
    board = []
    for i in range(rows):
        board.append(["0"] * cols)
    return board

def print_board(board):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rows = len(board)
    cols = len(board[0])
    print(f"  {[i+1 for i in range(cols)]}")
    for i in range(rows):
        print(f"{alphabet[i]}", end=" ")
        for j in range(cols):
            print(f" {board[i][j]} ", end="")
        print(" ")

def validate_coordinates(current_board, coordinate):    
    row, col = coordinate[0], coordinate[1]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        col = int(coordinate[1]) - 1  
        for letter in alphabet:
            if row == letter:
                row = alphabet.find(letter)
        if row < 0 or col < 0 or row > len(current_board[0]) or col > len(current_board):
            get_coordinates(current_board)
        else:
            if current_board[row][col] != '0':
                get_coordinates(current_board)  
        return row, col  

def get_coordinates(board):
    coordinate = input("Please enter your coordinate:(ex:A2): ").upper()
    if len(coordinate) != 2:
        coordinate = input("Try again. Place your coordinate:(ex:A2): ").upper() 
    while not coordinate[0].isalpha() or not coordinate[1].isnumeric():
        coordinate = input("Try again. Place your coordinate:(ex:A2): ").upper()
    (row, col) = validate_coordinates(board, coordinate)
    if validate_coordinates(board, coordinate) == False:
        get_coordinates(board) 
       
    return (row, col) 

def get_direction():
    valid_direction = ["left", "right", "up", "down"]
    direction = print("Now we choose the direction.")
    if direction == "left" or direction == "right" or direction == "up" or direction == "down":
        return direction
    while not direction in valid_direction:
        direction = input("Try again: left, right, up or down")
    return direction

def valid_coordinate_placing_boat(coordonate, direction, boat_length, current_board):
    (row, col) = coordonate
    ship_coordonates = [(row, col)]
    for ship_part in range(1, boat_length):
        if direction == 'right':
            ship_coordonates.append((row, col+1*ship_part))
        if direction == 'left':
            ship_coordonates.append((row, col-1*ship_part))    
        if direction == 'up':
            ship_coordonates.append(((row-1)*ship_part, col))
        if direction == 'down':
            ship_coordonates.append(((row+1)*ship_part, col))
        # else:
        #     ship_coordonates.append(((row+1)*ship_part, col))
    for ship_coordonate in ship_coordonates:
        (current_row, current_col) = ship_coordonate
        
    return ship_coordonates

def place_ships(current_board, ship_coordonates):
    row = len(current_board[0])
    col = len(current_board)
    for i in range(row):
        for j in range(col):
            pos = (i, j)
            for cord in ship_coordonates:
                if pos == cord and current_board[i][j] == "0":
                    current_board[i][j] = "X"
    return current_board             

def count_ship_on_board(current_player, current_board):
    number_of_x_in_board1 = 0
    for i in current_board:
        for j in i:
            if j == "X":# spatiu sters
                number_of_x_in_board1 += 1









# def count_ship_on_board(player1, board1, board2):
#     number_of_x_in_board1 = 0
#     number_of_x_in_board2 = 0
#     for i in board1:
#         for j in i:
#             if j == "X ":
#                 number_of_x_in_board1 += 1
#     for i in board2:
#         for j in i:
#             if i == "X ":
#                 number_of_x_in_board2 += 1

#     return number_of_x_in_board1, number_of_x_in_board2

# def get_size_of_ship():
#     print("You have 2 types of ships: 1 boat of 3 spaces(BIG), 1 boat of 2 space(TINY)")
#     valid_size = ["1", "2"]
#     size = input("choose 1 for Big, and 2 for Tiny")
#     while not size in valid_size:
#         size = input("try again: 1 or 2: ")
#     if size == "1":
#         return 3
#     if size == "2":
#         return 2   

# def validate_coordinates(board, coordinate):    
#     row, col = coordinate[0], coordinate[1]
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     while True:
#         col = int(coordinate[1]) - 1  
#         for letter in alphabet:
#             if row == letter:
#                 row = alphabet.find(letter)
#         if row >= len(board) or col >= len(board[0]):
#             return get_coordinates_for_boats(board)
#         return row, col


# def have_space(board, row, col, direction, ship_size):
#         if direction == "left":
#             return col - ship_size >= 0
#         if direction == "right":
#             return col + ship_size < len(board[0])
#         if direction == "up":
#             return row - ship_size >= 0
#         if direction == "down":
#             return row + ship_size < len(board)

# def is_available(board, row, col, ship_size):
#     for i in range(1, ship_size + 1):
#         if board[row][col] != "X":
#             return True
#         else:
#             return False


# def get_coordinates_for_boats():
#     coordinate = input("Please place your ship:(ex:A2): ").upper()
#     if len(coordinate) != 2:
#         coordinate = input("Try again. Place your ship:(ex:A2): ").upper() 
#     while not coordinate[0].isalpha() or not coordinate[1].isnumeric():
#         coordinate = input("Try again. Place your ship:(ex:A2): ").upper()
#     row, col = validate_coordinates(coordinate)  
#     return row, col 



# def get_direction(board, row, col, ship_size):
#     valid_direction = ["left", "right", "up", "down"]
#     direction = print("Now we choose the direction.")
#     direction = input("Try again: left, right, up or down")
#     if direction == "left" or direction == "right" or direction == "up" or direction == "down":
#         return direction
#     while not direction in valid_direction:
#         direction = input("Try again: left, right, up or down")
    

# def place_ships(board, ship_size, row, col, direction, max_ship1, max_ship2):
#     for i in range(ship_size):
#         if direction == "left":
#             board[row][col-i] = "X "
#         elif direction == "right":
#             board[row][col+i] = "X "
#         elif direction == "up":
#             board[row-i][col] = "X "
#         elif direction == "down":
#             board[row+i][col] = "X "

# def put_max_number_of_ships(player1, board1, board2, max_ship1, max_ship2):   
#     number_of_x_in_board1, number_of_x_in_board2 = count_ship_on_board(player1, board1, board2) 
#     if number_of_x_in_board1 == max_ship1 and number_of_x_in_board2 == max_ship2:
#         return True
#     else:
#         return False            
    


       