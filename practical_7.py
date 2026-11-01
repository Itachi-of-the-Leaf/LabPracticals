# backtracking search for 8-queens problem
#
# algorithm:
# 1. start placing queens from row 0 up to row 7
# 2. for current row, try placing queen in each column 0 to 7
# 3. check if column or diagonals conflict with placed queens
# 4. if safe, place queen and recursively move to next row
# 5. if all 8 queens placed, solution found
# 6. if placing fails, backtrack by removing queen and try next column

N = 8


def is_safe(board, row, col):
    # check column and diagonal conflicts with previously placed queens
    for prev_row in range(row):
        prev_col = board[prev_row]
        # same column
        if prev_col == col:
            return False
        # same diagonal
        if abs(prev_col - col) == abs(prev_row - row):
            return False
    return True


def solve_queens_backtracking(row=0, board=None):
    if board is None:
        board = [-1] * N

    # all queens placed successfully
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col  # place queen

            if solve_queens_backtracking(row + 1, board):
                return True

            board[row] = -1  # backtrack

    return False


def print_board(board):
    for r in range(N):
        row_str = " ".join("Q" if board[r] == c else "." for c in range(N))
        print(row_str)
    print()


if __name__ == '__main__':
    solution = [-1] * N

    if solve_queens_backtracking(0, solution):
        # 1-indexed representation matching manual
        one_indexed_solution = [col + 1 for col in solution]
        print("8-Queens Solution Found:")
        print("Column positions for each row (1 to 8):", one_indexed_solution)
        print("\nBoard Representation:")
        print_board(solution)
    else:
        print("No solution exists.")
