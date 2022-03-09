import Placing_phase
import Shooting_phase
import random


def main():
    game_mode, rows, cols = Placing_phase.start_menu()
    board = Placing_phase.create_board(rows, cols)
    if game_mode == "1":
        board1 = Placing_phase.create_board(rows, cols)
        board2 = Placing_phase.create_board(rows, cols)
        player1 = False
        player2 = True
        boat_lengths = [3, 2]
        for current_player, current_board in [(player1, board1), (player2, board2)]:
            for boat in boat_lengths:
                while True:
                    if not current_player: 

                        coordonate = Placing_phase.get_coordinates(board)
                        direction = Placing_phase.get_direction()
                    elif current_player:
                        coordonate = Placing_phase.get_coordinates(board)
                        direction = Placing_phase.get_direction()
                    else: #ai
                        coordonate = (random.randint(0, len(current_board[0])), random.randint(0, len(current_board)))
                        direction = ["left", "right", "up", "down"][random.randint(0, 1)]
                    
                    if Placing_phase.valid_coordinate_placing_boat(coordonate, direction, boat, current_board):
                        
                        ship_coordonates = Placing_phase.valid_coordinate_placing_boat(coordonate, direction, boat, current_board)
                        Placing_phase.place_ships(current_board, ship_coordonates)
                        Placing_phase.print_board(current_board)
                        break
                    
            print("Now Player 2:")
            if not current_player:
                current_player == False
        print("Now the shooting starts!!!")
        turn = 0
        while True:
            turn = turn + 1
            for (current_player, enemy_board) in [(player1, board2), (player2, board1)]:
                if [turn % 2]:
                    Placing_phase.print_board(enemy_board)
                    (shot_row, shot_col) = Shooting_phase.ask_shoot_coordinates(board)
                    if enemy_board[shot_row][shot_col] == 'X':
                        enemy_board[shot_row][shot_col] = 'H'
                    else: 
                        enemy_board[shot_row][shot_col] = 'M'
                        
                    if Placing_phase.count_ship_on_board(enemy_board) == 0:
                        print(f"Player {current_player} wins!!")
                        break
                
                
               


if __name__ == "__main__":
    main()        