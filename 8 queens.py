def solve_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row, board):
        if row == n:
            return True
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                if place_queens(n, row + 1, board):
                    return True
        return False

    board = [-1] * n
    if place_queens(n, 0, board):
        return board
    else:
        return None
n = 8
solution = solve_queens(n)
if solution:
    print("Solution found:")
    for i in range(n):
        print("Queen at row", i, "column", solution[i])
else:
    print("No solution found.")
