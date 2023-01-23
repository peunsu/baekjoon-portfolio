import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    result = -1
    while x <= m * n:
        if (x - y) % n == 0:
            result = x
            break
        else:
            x += m
    print(result)