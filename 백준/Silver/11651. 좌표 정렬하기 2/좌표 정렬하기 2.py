import sys

input = sys.stdin.readline

n = int(input())
pts = [tuple(map(int, input().split())) for _ in range(n)]
pts.sort(key=lambda x: x[0])
pts.sort(key=lambda x: x[1])

for x, y in pts:
    print(f"{x} {y}")