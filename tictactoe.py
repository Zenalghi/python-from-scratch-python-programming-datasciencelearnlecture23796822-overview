def print_board(board):
    for row in board:
        print(" | ".join(row)) #
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    for turn in range(9):
        print_board(board)
        print(f"Giliran pemain {current_player}. Masukkan baris dan kolom (0, 1, 2): ")
        
        while True:
            try:
                row, col = map(int, input().split())
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Posisi sudah terisi, coba lagi.")
            except (ValueError, IndexError):
                print("Input tidak valid, masukkan angka 0, 1, atau 2.")
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Pemain {winner} menang!")
            return
        
        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("Permainan seri!")

tic_tac_toe()
