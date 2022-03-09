def count_ship_on_board(player1, board1, board2):
    number_of_x_in_board1 = 0
    number_of_x_in_board2 = 0
    for i in board1:
        for j in i:
            if j == "X ":
                number_of_x_in_board1 += 1
    for i in board2:
        for j in i:
            if i == "X ":
                number_of_x_in_board2 += 1

    return number_of_x_in_board1, number_of_x_in_board2

def get_size_of_ship():
    print("You have 2 types of ships: 1 boat of 3 spaces(BIG), 1 boat of 2 space(TINY)")
    valid_size = ["1", "2"]
    size = input("choose 1 for Big, and 2 for Tiny")
    while not size in valid_size:
        size = input("try again: 1 or 2: ")
    if size == "1":
        return 5
    if size == "2":
        return 1   

def validate_coordinates(board, coordinate):    
    row, col = coordinate[0], coordinate[1]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        col = int(coordinate[1]) - 1  
        for letter in alphabet:
            if row == letter:
                row = alphabet.find(letter)
        if row >= len(board) or col >= len(board[0]):
            return get_coordinates_for_boats(board)
        return row, col

def is_ship_near(board, row, col, ship_size, direction):
    # for i in range(1, ship_size+1):
    # # row, col = len(board), len(board[0])
    #     if direction == "left:":
    #         if board[row][col-1] != "#": #and board[row-1][col] != board[0][col]: #pt left
    #             return True
    #     elif direction == "right":
    #         if board[row][col+1] != "#":#pt right
    #             return True
    #     elif direction == "up":
    #         if board[row-1][col] != "#": #pt up
    #             return True
    #     elif direction == "down":
    #         if board[row+1][col] != "#": #pt down
    #             return True
    #     else:
    #         return False
    for row_check in range(max([row - 1, 0]), min([row + 2, len(board[0])])):
        for col_check in range(max([col - 1, 0]), min(col + 2, len(board))):
                if not str(board[row_check][col_check]).isnumeric() and not (row_check == row and col_check == col):
                    return True
    return False
# for row_check in range(max([row - 1, 0]), min(row + 2, len(board))):
#             for col_check in range(max([col - 1, 0]), min([col + 2, len(board[0])])):
#                 if not str(board[row_check][col_check]).isnumeric() and not (row_check == row and col_check == col):
#                     return True
#     return False

def have_space(board, row, col, direction, ship_size):
        if direction == "left":
            return col - ship_size >= 0
        if direction == "right":
            return col + ship_size < len(board[0])
        if direction == "up":
            return row - ship_size >= 0
        if direction == "down":
            return row + ship_size < len(board)

def is_available(board, row, col, ship_size):
    for i in range(1, ship_size + 1):
        if board[row][col] != "X":
            return True
        else:
            return False

    # def verify_right_left(board, start, stop):
    #     for i in range(start, stop):
    #         if not str(board[row][i]).isnumeric() or is_ship_near(board, row, i):
    #             return False
    #     return True
    
    # def verify_up_down(board, start, stop):
    #     for i in range(start, stop):
    #         if not str(board[i][col]).isnumeric() or is_ship_near(board, i, col):
    #             return False
    #     return True

    

    # available_options = []
    # if have_space("left"):
    #     if verify_right_left(board, col - ship_size, col + 1):
    #         if "left" not in available_options:
    #             available_options.append("left")
    # if have_space("right"):
    #     if verify_right_left(board, col, col + ship_size + 1):
    #         if "right" not in available_options:
    #             available_options.append("right")
    # if have_space("up"):
    #     if verify_up_down(board, row - ship_size, row + 1):
    #         if "up" not in available_options:
    #             available_options.append("up")
    # if have_space("down"):
    #     if verify_up_down(board, row, row + ship_size + 1):
    #         if "down" not in available_options:
    #             available_options.append("down")
    # return available_options


def get_coordinates_for_boats(board, ship_size):
    coordinate = input("Please place your ship:(ex:A2): ").upper()
    if len(coordinate) != 2:
        coordinate = input("Try again. Place your ship:(ex:A2): ").upper() 
    while not coordinate[0].isalpha() or not coordinate[1].isnumeric():
        coordinate = input("Try again. Place your ship:(ex:A2): ").upper()
    row, col = validate_coordinates(board, coordinate)
    direction = get_direction(board, row, col, ship_size)
    while not is_available(board, row, col, ship_size):
        coordinate = input("place taken. try again!!: ")
    while not is_ship_near(board, row, col, ship_size, direction):
        coordinate = input("too close. Try again: ")   
    return row, col, direction  



def get_direction(board, row, col, ship_size):
    valid_direction = ["left", "right", "up", "down"]
    direction = print("Now we choose the direction.")
    direction = input("Try again: left, right, up or down")
    if direction == "left" or direction == "right" or direction == "up" or direction == "down":
        return direction
    while not direction in valid_direction:
        direction = input("Try again: left, right, up or down")

    # if col == 0:
    #     direction = input("choose direction: possible only: up, down, right: ")
    #     return direction
    # elif col == board[row-1]:
    #     direction = input("choose direction: possible only: up, down, left: ")
    #     return direction
    # elif row == 0:
    #     direction = input("choose direction: possible only: down, left, right: ") 
    #     return direction
    # elif row == len(board[-1]):
    #     direction = input("choose direction: possible only: up, left, right: ")
    #     return direction          
    
 
    

def place_ships(board, ship_size, row, col, direction, max_ship1, max_ship2):
    for i in range(ship_size):
        if direction == "left":
            board[row][col-i] = "X "
        elif direction == "right":
            board[row][col+i] = "X "
        elif direction == "up":
            board[row-i][col] = "X "
        elif direction == "down":
            board[row+i][col] = "X "

def put_max_number_of_ships(player1, board1, board2, max_ship1, max_ship2):   
    number_of_x_in_board1, number_of_x_in_board2 = count_ship_on_board(player1, board1, board2) 
    if number_of_x_in_board1 == max_ship1 and number_of_x_in_board2 == max_ship2:
        return True
    else:
        return False            
    


       