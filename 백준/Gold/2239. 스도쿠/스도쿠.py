import sys
input = sys.stdin.readline


def solve_sudoku(n: int):
    if n == 81:
        for i in range(9):
            print(*sudoku[i], sep="")
        exit(0)

    x = n // 9
    y = n % 9
    if sudoku[x][y]:
        solve_sudoku(n+1)
    else:
        for i in range(1, 10):
            if not row[x][i] and not column[y][i] and not square[x//3][y//3][i]:
                sudoku[x][y] = i
                row[x][i] = column[y][i] = square[x//3][y//3][i] = 1
                solve_sudoku(n+1)
                sudoku[x][y] = 0
                row[x][i] = column[y][i] = square[x//3][y//3][i] = 0

sudoku = [list(map(int, input().rstrip())) for _ in range(9)]
row = [[0] * 10 for _ in range(9)]
column = [[0] * 10 for _ in range(9)]
square = [[[0] * 10 for _ in range(3)] for _ in range(3)]

for i in range(9):
    for j in range(9):
        if temp := sudoku[i][j]:
            row[i][temp] = 1
            column[j][temp] = 1
            square[i//3][j//3][temp] = 1

solve_sudoku(0)