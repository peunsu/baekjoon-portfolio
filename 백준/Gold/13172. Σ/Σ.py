import sys
input = sys.stdin.readline
X = 1000000007


m = int(input())
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    a = pow(a, -1, X)
    result += (a * b)
    result %= X

print(result)