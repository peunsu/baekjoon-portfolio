import sys

def combination(n: int, r: int):
    result = 1
    for i in range(n-r+1, n+1):
        result *= i
    for j in range(1, r+1):
        result //= j
    return result

input = sys.stdin.readline

n = int(input())

total = 0
for i in range(n // 2 + 1):
    total += combination(n-i, i)
print(total % 10007)