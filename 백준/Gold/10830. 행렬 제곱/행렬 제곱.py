import sys
input = sys.stdin.readline

def matmul(A: list, B: list):
    return [[sum(a*b for a, b in zip(A_row, B_col)) % 1000 for B_col in zip(*B)] for A_row in A]

def matsquare(A: list, n: int):
    if n == 1:
        return matmul(A, UNIT_MAT)

    if n % 2 == 0:
        temp = matsquare(A, n//2)
        return matmul(temp, temp)
    else:
        temp = matsquare(A, n-1)
        return matmul(A, temp)

n, b = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
UNIT_MAT = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

result = matsquare(mat, b)

for row in result:
    print(*row)