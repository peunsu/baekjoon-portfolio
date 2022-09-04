import sys
n = int(input())
pts = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
pts.sort()
for a, b in pts:
    sys.stdout.write(f"{a} {b}\n")