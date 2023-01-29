import sys
input = sys.stdin.readline

def factorial(n: int) -> int:
    if n == 0:
        return 1
    
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

def combination(n: int, m: int) -> int:
    return factorial(n) // (factorial(n-m) * factorial(m))

n, m = map(int, input().split())

print(combination(n, m))