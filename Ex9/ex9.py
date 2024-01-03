import sys


def Board(n):
    B = []
    for i in range(n):
        B.append([])
        for j in range(n):
            B[i].append(0)

    return B


def PB(board):
    for i in board:
        print(' '.join(map(str, i)))


def isSave(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def NQueens(N):
    def solveNQueens(board, col):
        if col >= N:
            solutions.append([row[:] for row in board])
            return

        for i in range(N):
            if isSave(board, i, col, N):
                board[i][col] = 1
                solveNQueens(board, col + 1)
                board[i][col] = 0

    board = Board(N)
    solutions = []
    solveNQueens(board, 0)

    for solution in solutions:
        PB(solution)
        print()

    return len(solutions)


if len(sys.argv) == 2 and sys.argv[1].isdigit():
    n = int(sys.argv[1])
    print(f'Argument is {n}.')
    print()
else:
    n = 8
    print(f'Unknown argument, use default which is {n}')
    print()
numSolutions = NQueens(n)
print(f'There is {numSolutions} ways to solve {n} Queens problem.')
