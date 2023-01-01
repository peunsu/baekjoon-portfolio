import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)][::-1]
cnt = 0

for c in coins:
    cnt += k // c
    k %= c

print(cnt)