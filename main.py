import Placing_phase
import Shooting_phase


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
        board.append(["0 "] * cols)
    return board

def print_board(board):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rows = len(board)
    cols = len(board[0])
    print(f" {[i+1 for i in range(cols)]}")
    for i in range(rows):
        print(f"{alphabet[i]}", end=" ")
        for j in range(cols):
            print(f"{board[i][j]} ", end="")
        print(" ")

def place_ships_part(player1, board1, board2, max_ship1, max_ship2):
   
    # if max_ship1 == 0 and max_ship2 == 0:
    #     return None
    # 
    # if player1 and max_ship1 == 0:
    #     input("You've put Ur boat. Now wait for Player 2.")
    #     return place_ships_part(board1, board2, max_ship, not player1)
    # if not player1 and max_ship2 == 0:
    #     input("You're done. Wait for player 1 to place his ships.")
    #     return place_ships_part(board1, board2, max_ship, not player1)
    while True:
        if Placing_phase.put_max_number_of_ships(player1, board1, board2, max_ship1, max_ship2) == False:
            if player1 and max_ship1 == 0:
                input("Done. All ships on map. Wait for player 2 to finish.")
                return place_ships_part(board1, board2, max_ship1, max_ship2, not player1)
            if not player1 and max_ship2 == 0:
                input("Finished with placing the ships. Now you wait for player 1 to finish.")
                return place_ships_part(board1, board2, max_ship1, max_ship2, not player1)    
            print(f"Player {1 if player1 else 2}")
            print_board(board1 if player1 else board2)
            print(" ")
            print(f"Player {1 if player1 else 2} , make your move:")
            ship_size = Placing_phase.get_size_of_ship()
            # print(f"You have left {max_ship1 if player1 else max_ship2} ship spaces to place")
            row, col, direction = Placing_phase.get_coordinates_for_boats(board1 if player1 else board2, ship_size)
            ship_on_map = Placing_phase.place_ships(board1 if player1 else board2, ship_size, row, col, direction, max_ship1, max_ship2)
            print_board(board1 if player1 else board2)
            input(f"Press enter to continue to player {2 if player1 else 1}")
            # place_ships_part(board1, board2, max_ship1, max_ship2, not player1)
        else:
            return board1, board2 


def shoot_ships_part():
    pass

def main():
    game_mode, rows, cols = start_menu()
    # board = create_board(rows, cols)
    # print_map = print_board(board)
    if game_mode == "1":
        max_ship1 = 5
        max_ship2 = 5
        board1 = create_board(rows, cols)
        board2 = create_board(rows, cols)
        player1 = True
        play = place_ships_part(player1, board1, board2, max_ship1, max_ship2)
            # print(f"Player's {player+1} turn: ")
            # while max_ship > 0:
                
            
        #     ship_on_map = Placing_phase.place_ships(board, ship_size, row, col, direction, max_ship)
        #     map = print_board(board)
        #     max_ship = max_ship - ship_size
        #     print(f"You have left {max_ship} ship spaces to place")
        #     if max_ship == 0:
        #         continue
        # player == 2 if player == 1 else 2

#  def play(board, player):
#     print_board(board)
#     while True:
#         rows, cols = get_move(board, player)
#         if mark(board, player, rows, cols):
#             break
#     if has_won(board, player):
#         print_board(board)
#         print_result(player)    
#     elif is_full(board):
#         print_board(board)
#         print_result(None)
#     else:
#         play(board, "X" if player == "O" else "O")             


if __name__ == "__main__":
    main()        