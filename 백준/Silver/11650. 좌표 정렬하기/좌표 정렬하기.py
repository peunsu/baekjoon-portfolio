n = int(input())
pts = [list(map(int, input().split())) for _ in range(n)]
pts.sort()
for a, b in pts:
    print(f"{a} {b}")