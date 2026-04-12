board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

player = "X"


def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")


def player_input(board, player):
    while True:
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter col (0-2): "))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input, try again")

        elif board[row][col] != " ":
            print("This place is already taken")

        else:
            return row, col


def check_win(board, player):
    # check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # check main diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    # check other diagonal
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True


def play():
    global player

    while True:
        display_board(board)

        row, col = player_input(board, player)
        board[row][col] = player

        if check_win(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"


play() 