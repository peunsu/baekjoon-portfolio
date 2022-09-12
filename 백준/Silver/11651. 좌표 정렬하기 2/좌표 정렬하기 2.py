import sys

input = sys.stdin.readline

n = int(input())
pts = [tuple(map(int, input().split()[::-1])) for _ in range(n)]
pts.sort()

for y, x in pts:
    print(f"{x} {y}")