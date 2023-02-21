import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def matmul(A, B):
    return [[sum(a * b for a, b in zip(row_A, col_B)) % 1_000_000_007 for col_B in zip(*B)] for row_A in A]

def matsquare(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        temp = matsquare(A, n//2)
        return matmul(temp, temp)
    else:
        temp = matsquare(A, n-1)
        return matmul(A, temp)

n = int(input())
fibo = [[1, 1], [1, 0]]

print(matsquare(fibo, n)[0][1])