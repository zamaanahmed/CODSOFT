import math

# Initialize the board
def initialize_board():
    return [' ' for _ in range(9)]

# Print the board
def print_board(board):
    for row in range(3):
        print('|'.join(board[row*3:(row+1)*3]))
        if row < 2:
            print('-----')

# Check if the board is full
def is_board_full(board):
    return ' ' not in board

# Check for a win
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Get valid moves
def get_valid_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'X'):
        return -1
    if check_win(board, 'O'):
        return 1
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_valid_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_valid_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Get the best move for the AI
def get_best_move(board):
    best_move = None
    best_value = -math.inf
    for move in get_valid_moves(board):
        board[move] = 'O'
        move_value = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = ' '
        if move_value > best_value:
            best_value = move_value
            best_move = move
    return best_move

# Main game loop
def play_game():
    board = initialize_board()
    current_player = 'X'  # Human starts first

    while True:
        print_board(board)
        if current_player == 'X':
            # Human move
            move = int(input("Enter your move (0-8): "))
            if board[move] == ' ':
                board[move] = 'X'
                if check_win(board, 'X'):
                    print_board(board)
                    print("You win!")
                    break
                current_player = 'O'
            else:
                print("Invalid move. Try again.")
        else:
            # AI move
            move = get_best_move(board)
            board[move] = 'O'
            if check_win(board, 'O'):
                print_board(board)
                print("AI wins!")
                break
            current_player = 'X'

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

# Run the game
play_game()
